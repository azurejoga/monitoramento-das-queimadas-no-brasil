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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f9532cd-461b-31b1-b397-148b70575e2c | -5.08757 | -46.20325 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a12a43e-73f9-3e84-84e5-c504e60896a3 | -2.4033 | -57.89666 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ce27f6d-60d3-3ecd-b650-79a3f7651733 | -5.10162 | -46.22382 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 550cf339-7169-34f6-be0e-62b3d4c7a05d | -5.60093 | -47.28345 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47c96f57-3394-3051-b037-0ef9ffafe585 | -3.04604 | -54.15997 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fe95b98-a026-3ad1-a60f-e85a07e193c0 | -2.15675 | -45.87928 | 2026-10-10 04:44:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21844c20-7fa3-3878-a263-8b101f5ae8e2 | -2.20514 | -46.44371 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48059e1d-f154-361d-8eec-b766d978ab26 | -3.56283 | -54.69507 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fd5b715-3384-3039-8120-627e643627b8 | -2.78966 | -51.40978 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7564b8e6-58e2-3702-b426-e400bce0c3f6 | -5.99244 | -41.37017 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 992b041c-aa2e-33bd-984b-47aae8334632 | -2.92782 | -54.07798 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8cdc3d6-8801-3445-9cb9-414ecf07ed96 | -6.06501 | -44.65887 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c909d2a4-52be-368b-a2c1-059a6f8b3252 | -5.95728 | -40.91937 | 2026-10-10 04:44:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6806bb53-9561-32b4-86e0-02c3f2c76a71 | -3.58207 | -54.69848 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 171da2e1-7777-3fa7-a7ca-9ae9ce7b13a6 | -3.26946 | -54.05317 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60fab820-ea4f-37d1-800e-3a9cbe0ed375 | -5.76471 | -41.63654 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fa882927-d22f-39a4-942e-34008271d0c2 | -7.19181 | -42.00023 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a4b6fea-1355-3465-ad05-293f8f925973 | -3.27642 | -50.39253 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b76c86b-8145-3861-8a29-3ffaa192750b | -3.50165 | -49.94562 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24aec84a-f5bd-3da5-95a3-90abfb8f091d | -3.47549 | -46.06984 | 2026-10-10 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 759fd23b-f965-324f-9136-3c60b96df8b7 | -2.56763 | -57.41246 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 127b62c3-7720-32f6-9d2b-b0293cc0f186 | -6.48662 | -43.62768 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84a93327-6db1-39f7-9ada-ef607282c710 | -5.89372 | -45.59383 | 2026-10-10 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36f951bd-e06d-38d0-be96-e2510620d63c | -3.54409 | -54.6957 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b046d33-bed4-313d-b99e-bc544619492b | -3.34991 | -50.41983 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc912cca-a942-3602-899b-838f17908862 | -4.73688 | -55.6769 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fb66bcf-868d-3aab-8ae6-12e9babb65fc | -2.47741 | -56.09106 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96fa09f2-59d6-3f2a-87c5-e4ac20bcae62 | -3.2717 | -54.06829 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80e4ff7d-b347-3db2-91b7-60c0aa78c4aa | -1.62385 | -54.42889 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad44bc0b-5f43-3e63-a57d-4b2acaaa0bb4 | -3.00795 | -54.04386 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 010f6811-bdf1-3011-8f81-7e347be26ec1 | -4.12858 | -50.8348 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f39954f4-cf51-3f92-9c75-b34ca75e9b4c | -3.74658 | -59.40261 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2606f5fc-bf5a-324e-9fff-2fc845cd6102 | -3.34624 | -50.41924 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b2a4426-ce53-342e-a671-c8196c8dbcf3 | -3.89278 | -52.19505 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b74f5baf-508e-3ace-b121-e8d7fd7aee85 | -5.75309 | -45.12247 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a75abc1c-d2ff-3df3-9e6c-2f9dc14b42af | -5.79027 | -53.8069 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cec858b1-7254-36cc-8ca4-8d85df570176 | 0.9455 | -50.20159 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb967764-3746-3552-9aab-bba27ba4c57c | -3.3702 | -59.38514 | 2026-10-10 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 501e2ece-9656-3601-9103-61a736cb86c2 | -6.64569 | -43.44954 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d99c7969-57d9-35d9-87c2-08ca1c5e963b | -6.20656 | -45.42733 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0a5dc5c-a23e-3e5f-906e-47af027e11b1 | -4.05375 | -54.45556 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3418dc3f-d017-3dbd-a46b-e855ad088475 | -3.22441 | -49.4298 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 6d1f9781-d93e-3b4b-a151-4fed2d7528f2 | -4.09316 | -54.00092 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d27c962-e321-3088-b7ec-3caeb66b25f1 | -3.25572 | -54.02152 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c60f9512-1ce3-37c9-ae58-5a006a3ef4ef | -4.63739 | -50.96218 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c41dee4-d7bc-31ea-b871-748bdee51796 | -3.55059 | -54.68626 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04704df9-702a-3a2f-a0c4-113101085cbb | -3.93376 | -55.72838 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbc1c7ef-77f6-3367-a7bb-8cd74c8a2618 | -3.56941 | -54.6855 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d95f39-3542-3474-9ce5-37896f50f8b8 | -2.93106 | -54.0586 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db174862-b673-3125-898f-154eb1c450d8 | -2.74227 | -54.10228 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de0ec60d-6c20-33eb-828d-cc7f0d91a874 | -3.56756 | -54.67316 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bb8a478-fec9-394f-b0e3-95e2624ad629 | -5.69993 | -49.0514 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0732f7ad-d5b3-3069-a06d-932107a883c9 | -2.73029 | -54.14581 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 00081cb0-a4e5-3836-a22e-691fd592c64a | -5.74898 | -45.12588 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ecfdec24-67cb-31b6-93a2-bb5a04929f51 | -5.68886 | -53.47025 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fb9f788-6f7c-3ea9-bc52-f00bf613a18b | -4.40612 | -49.77406 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 255770be-1018-37be-8cac-4bee27d0b055 | -3.25191 | -50.42807 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d393b40a-0313-318c-b265-3d406a7945f5 | -4.82418 | -56.07976 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ee288ce-9c87-3a14-8d23-223bc09d63c9 | -3.01338 | -54.05242 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 406525b7-484c-31f1-87d6-092825378357 | -5.67303 | -50.08178 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f947ca5-e594-342b-9192-de8da55a8188 | -3.24947 | -54.03045 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dc3107e-ae95-3018-947f-26a5c2d2eb64 | -3.27276 | -50.39194 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d5a6f1a-1cff-39ae-8036-34981c604841 | -3.72938 | -59.46203 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 816379cb-635a-3633-a155-e3a9e1cab692 | -3.87269 | -55.98934 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37a2b47b-1f49-3340-9706-e13232925026 | -6.41901 | -44.07143 | 2026-10-10 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 311c05c0-ede8-3096-8537-35d7aae13c1d | -6.15487 | -47.11741 | 2026-10-10 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfad7dfe-1968-3796-a225-1c93a9e2b798 | -3.76467 | -45.95878 | 2026-10-10 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6390a1b3-952a-358d-b980-bf442c23dd96 | -3.29794 | -54.08255 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f390cccf-8f58-30c3-92c1-48a169b0ba67 | -4.11084 | -54.92816 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09db3ff4-d447-39d4-a7ab-64dd46963fc7 | -5.11231 | -46.22181 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87dadb7c-b204-30cb-82d6-42433c2032ae | -7.21293 | -44.3512 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e059d545-177e-3e2e-a869-18a7fbb797bc | -5.69154 | -53.46955 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6f123e1-b8b7-3c73-acd9-e0aa2199c215 | -7.21123 | -44.33723 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87e634b2-dc58-3fd9-b96c-d6ebc7eac521 | -3.16475 | -50.59166 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fb88f64-74e6-3ca3-a63f-d7bac67658ad | -3.25778 | -54.18089 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a99f0112-d07e-346a-bbf6-47dffd98e3cc | -3.00951 | -54.04681 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99c8be40-7759-3717-8543-4a5402ded9fa | -3.26401 | -54.05726 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1e89971-cde0-3e57-9540-6158cd512f4d | -2.46403 | -56.05899 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed71bb67-6847-3d0a-9598-7412b09996d5 | -4.10074 | -56.13143 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8874939d-49ed-399a-be67-a66502a9c9ee | -4.10822 | -54.02249 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| debdc61a-bc68-3e36-87ff-76c0c1e6c9ba | -3.90535 | -58.9577 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a53ed058-fdd2-3af6-959c-a5c41fd28b72 | -2.99726 | -53.91745 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a8f5969-889c-333f-bb75-af598a88e84f | -3.11247 | -51.68736 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f87e47b-a03b-33f2-846c-0e6079f78181 | -3.18021 | -48.58405 | 2026-10-10 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba7f1180-c1d8-35cc-b002-78c9bfd600df | -3.7914 | -59.37682 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c2a25c1-3411-36d1-9e2b-e0e26104bbf2 | -5.87555 | -53.51268 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d508c75d-cb56-3459-9201-54151d49e3f4 | -2.61024 | -51.70646 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93f1a265-d814-36be-98ba-795e70507faf | -3.40243 | -49.09087 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aacfc98-bd1e-390f-859f-64e4bcb4dee7 | -3.77372 | -60.71918 | 2026-10-10 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe12f1ef-cc94-368b-8bf4-e44448b6f84b | -5.93288 | -52.18159 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3e3659-5901-3ee7-bf61-1a366fe0fcf8 | -3.22275 | -49.4386 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532d8eda-65b9-3f6e-8d15-2965c2d659bd | -0.97857 | -52.44223 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e66c7cad-d7e8-3ea2-840e-d42a21612e70 | -3.00764 | -51.00674 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 911a4886-4d0b-3f42-be19-797357080316 | -5.23753 | -50.89992 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3bdbaec-d54c-345e-aa20-1797c09b0c90 | -5.08814 | -46.19962 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f3cf7a4-01f2-35d1-bce8-3e6e4b2fc5c5 | -3.56193 | -54.70034 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 375415f5-528e-3654-816a-20f098883797 | -2.93635 | -54.08436 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6a5fe936-2688-3df3-9ae3-3aeb51cfed84 | -3.1706 | -58.62038 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a1d87c5-08e3-3aed-a134-784bf1d04a0d | -4.91973 | -45.78148 | 2026-10-10 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b665175f-0186-37ab-8bc7-3c786057d568 | -2.88893 | -54.06994 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README62.md)
