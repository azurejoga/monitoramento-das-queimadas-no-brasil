# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57bd7aa2-4123-3ca5-b6ae-c9e97939653c | -3.58052 | -54.71707 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55d41827-c09f-3ee1-bf95-cdbf4fe8bf7c | -4.81672 | -56.08521 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29a81922-f381-3cf0-b09a-487266f9d220 | -3.02133 | -57.7801 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e36f6990-e2ba-346e-bed3-20b6b5f9979a | -1.95827 | -54.39898 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01dfebd3-4a78-3751-9d2a-ca70bf317ca4 | -2.38802 | -57.89695 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cce0ff82-18cf-3096-a5ff-7f311e69211e | 0.31539 | -60.43758 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26558e30-a514-3f7f-817c-c1da7596f9c9 | -3.94322 | -56.05311 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a5cd950-ad41-3f73-a4d3-4f14ec554871 | -1.11394 | -54.16972 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c76249a-926f-386e-a3e4-f220ecc7a563 | -3.43541 | -54.53618 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fef31fdf-3ca1-3e86-9b5e-9017359fc5ef | -2.5052 | -56.20642 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d11c623b-f326-3b3c-a8a7-88c24604f7b7 | -3.12168 | -54.17119 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94d47f4e-d722-3f74-87e7-fe1b022b3826 | -3.65658 | -59.1711 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd28aa21-be73-3e5d-8339-a589844b1490 | -3.81475 | -59.33551 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87450452-31b6-3bfb-834c-29e9ef3a8b69 | -5.99166 | -55.36749 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f0198e4-6c8e-3559-a78f-fd7f01889951 | -2.94214 | -54.07939 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1379ee7d-dac4-38f2-8989-e0e1a323ea69 | -5.0897 | -60.22017 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fa4a4e5-1a61-3500-b2d2-90b4e2a21158 | -4.10458 | -54.01722 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf1dbc9e-4bee-336b-8be3-90ae041990c4 | -2.98816 | -54.17485 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 486c61b1-8149-321a-ac3b-2c6b90169397 | -2.5637 | -57.42194 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6e21a5b-780a-3a02-b6c2-cf49a145b258 | -2.85919 | -59.11294 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50b7c272-193f-3a6f-96a0-3c36ef393a6f | -3.74023 | -58.49963 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8ec3ce0a-a5aa-3296-b206-e229b3e4f19e | -5.18999 | -60.30589 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59159b75-9b47-3533-aff3-e96cbc8eb8f8 | -2.52801 | -56.27045 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41e1cf2f-8641-3760-ae34-13a092e89567 | -3.06941 | -59.17066 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e05c5dbc-689f-391c-90a6-20b7f0edb30f | -5.99231 | -55.36263 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7a08fa-dd12-3b53-92c2-e853b610ada1 | -3.56961 | -54.3844 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2a23ebdb-cdcb-374a-b00c-72e197ec5490 | -3.31273 | -54.67249 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9a306425-cf43-34b7-b8f4-f2df4a309d1b | -2.84836 | -59.12136 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76043ef7-fee0-3c0d-bcf5-782432622f49 | -3.28361 | -53.86899 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e36ad1bd-b706-326b-91ca-78d218238033 | -3.99135 | -59.35355 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 182ea759-e926-337e-9540-268b93dd639f | -5.07567 | -60.22258 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dc05f13b-54bc-3142-b2e2-e6984bc12616 | -3.64043 | -59.56691 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d054953-075d-330f-8e78-ec66fac867df | -6.45331 | -55.28493 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7073cc9d-8550-3353-b234-4abdf20c5516 | -3.95948 | -55.34342 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6070669-6592-3df0-a757-087920311cc9 | -3.90451 | -58.95167 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aea10cf6-5428-3947-966c-a644dc85b782 | -1.21347 | -55.66047 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77eafd3d-8c12-321a-a9a7-5cc1755ee8f7 | -3.99455 | -59.36406 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 042705c6-24ea-34ae-9602-4d5221c14194 | -1.5151 | -54.5208 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c94515c4-be62-3361-8afe-c47a7e3879b7 | -3.07771 | -59.2761 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 416c36c4-059d-3394-b642-a86b7256a5c1 | -1.19456 | -55.66156 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89cf2545-870f-334f-a803-525b060c030c | -3.3147 | -54.68145 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98198a7c-6144-3356-9023-3d2425bf8dc2 | -4.35243 | -59.95047 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ff52a43-bfdd-3a37-ac9f-ae9352b3d418 | -3.73188 | -59.45499 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00e6de21-db5c-3729-91e5-8adc7c4e9e29 | -3.59918 | -54.58885 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d5705e8-c89e-3c47-8afa-777f8e2a3803 | -3.27974 | -54.70105 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5000d467-3f84-3a91-b182-4745ef752aaf | -3.00126 | -58.89855 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f78c687a-f0ca-35b3-b124-bed4cbb74d52 | -4.52569 | -61.13227 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c48807e-e3d6-3e5e-ba10-3ef3f66c191c | -3.57715 | -59.07616 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e69492f-7a1b-3859-8077-909c0328b1d6 | -2.45571 | -57.8923 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e495ffcd-9198-3f15-98a5-773a7e0b15ae | -3.53138 | -59.57608 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3da4cb36-13b2-3f40-a139-d2218299d74f | -5.22671 | -60.04921 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d006162-ff8e-3532-b516-29ba881886ad | -2.56491 | -57.41979 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f37ff016-2ec2-3291-a8a8-6c0e26181d5e | -2.3876 | -57.89981 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c059d04-a410-3084-9384-b1f97157a091 | -3.03482 | -59.15887 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c100250a-17d5-3b77-926b-416b5cbb591f | -3.001 | -53.91214 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b93dc0f3-53c4-3e87-912d-a91ba76affaa | -3.07908 | -59.13702 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9be50424-24ec-305e-aaf9-50759532edc9 | -5.97744 | -55.34903 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e6c6f61-e4ca-300a-9535-3846dbbc9589 | -3.00016 | -53.91768 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 625006e3-f223-381d-8291-2cd14f0e7967 | -3.43709 | -59.35567 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27443f5a-d555-39de-8e31-99281d50836e | 0.30785 | -60.44241 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 208f03a1-9f40-3bc2-8945-ce22e8f52322 | -2.39852 | -57.89557 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8455fd27-162c-3aaf-937c-b5542785b8b7 | -3.63458 | -59.57273 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f497349c-b00f-3125-a207-cc2e65c11068 | -3.78161 | -59.24874 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32abff26-5ce8-3428-acd8-6733ee5096f3 | -3.98437 | -54.45699 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5856c3d-b100-3543-89d3-b0d179713d7e | -0.51743 | -58.09628 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f04196c1-e39d-3948-80c2-fdde16b7ffb6 | -3.91111 | -55.82171 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f23594a8-5b19-3c64-a441-6465e20ea68a | -3.58027 | -58.63176 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a80f8fda-2892-3032-9f8f-76b757681bdb | -3.56472 | -59.09482 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92e73399-5478-3225-ac6a-441e55421624 | -2.49908 | -58.08361 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55f5cd4b-2684-31ef-b6b0-597c1c5ca45d | -5.96625 | -55.33748 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fa4d5c6-e363-3703-a2a2-a95a494c66ac | -1.21979 | -55.65751 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc3cba25-94f5-36ac-af49-91238a350a84 | -3.56524 | -54.68884 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9acb375d-fa9f-3747-a0f8-107749ee359d | -2.73226 | -54.14999 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f89251f-bbd1-341d-8687-e1a71e511d28 | -3.74507 | -59.39799 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a6f02b4-eee5-3b6d-a7e3-6a2c491f170d | -1.63659 | -54.41177 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1f7c2e9-d9b9-3650-8a54-e20d372ce85a | -3.7581 | -59.62944 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 873268d2-f8c8-3973-9e9f-4f9424d85be3 | -3.75812 | -59.46878 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 541b5ccc-d459-35ac-a0ee-46fe2308c646 | -2.84443 | -59.11585 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8b7003e-de5e-3ad2-afa8-3a1eeb9d8c21 | -1.89083 | -54.69028 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| acb5fad7-bc48-3082-80d6-0276ae62de65 | -1.21238 | -55.66048 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a9ca0ee-ef31-3915-b58e-36a89f93ffc8 | -3.22358 | -54.2911 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a884fb9-1328-33d0-a226-5c50ea17ff8c | -0.98232 | -52.44181 | 2026-10-10 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3ada73ae-a695-3d64-8c0f-47aafe5bd61c | -1.20703 | -54.21594 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 855a9580-d13e-331f-948f-6e71270ade1f | -3.58682 | -54.71812 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6eda771-7bc7-3af0-842b-0d5a86737ae3 | -3.99381 | -59.36897 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b03dbb98-640e-3ab6-b67f-4311d932a443 | -2.75254 | -54.10334 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44377a68-978a-3a02-82ac-4033ca529630 | -0.00076 | -60.57739 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81d91bb3-b01f-31a4-8759-54d303798536 | -5.064 | -60.25048 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b947186-30e9-3e66-a89d-32fff74f4bdf | -5.18872 | -60.31471 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63d11fdc-12aa-313e-854f-9b7d55fcbf32 | -1.27613 | -55.75104 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b415657-f060-3545-9d25-56378e6ff417 | -5.97051 | -55.35286 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d15669-4e64-3c27-9a28-ad7f18237d6b | -3.75421 | -59.62408 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e20f4ef-3778-3e41-af0a-9ed66ed825db | -5.08524 | -60.21949 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9fa459c6-19a3-347c-a4dd-2fd574b78577 | -3.25975 | -54.18071 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9bd7685b-4020-31b9-8a3f-236342d9d176 | -3.98449 | -59.36757 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3c66a8db-6c6b-3c78-90f3-2a0e93e4b44a | -5.79775 | -53.79385 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39f6f5b5-bfc6-354f-9703-c590a95f604f | -1.95314 | -54.40871 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aa33e15-8ea8-3df0-9622-d2944d475f82 | -3.7528 | -59.47284 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ddf0dcf-7daf-30ea-9691-404721daba53 | -2.93486 | -54.08383 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b075a932-3f5b-3f3d-a0dd-b298f35b5a8e | -1.9547 | -54.39855 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README142.md)
