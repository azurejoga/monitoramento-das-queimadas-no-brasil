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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9916c4c0-2c24-30e1-b67a-543154b4dafa | -3.00632 | -57.90071 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e66a8ff1-ab2b-3565-9533-66b20c3684f3 | -3.14798 | -51.62698 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19f599bd-d76b-37ea-a0c7-cdbfe07d818c | -3.05291 | -51.22502 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9397eaa8-a15f-34be-bf71-a5e71b765071 | -3.05927 | -54.22121 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13e323f-6f57-3ac6-b835-73750ebaf017 | -4.07417 | -59.83686 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dbe5b566-da8c-326b-a5b4-28ee467f4bfe | -3.67633 | -54.49853 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e4ad81b-2432-34ef-9a36-a0555f277ec4 | -3.48143 | -59.57944 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c895f5e-f856-360f-8837-1bc98282cc45 | -2.15711 | -59.22807 | 2026-10-08 05:23:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5f65d92-b3cd-3b38-8dbf-3b84badd728d | -4.27193 | -54.86517 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b49332fe-3cb8-3152-904c-2fc1c7627af7 | -3.56853 | -54.48712 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5fc2fc6-46aa-3e83-a901-0c3b25f4577a | -3.14651 | -53.72735 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e6a0bf2-9f8b-3049-abfc-f0aff53f275a | -3.25593 | -50.39494 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca71390-97a5-348c-ad7e-c3b717d7c439 | -3.74106 | -59.46969 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 108ef8dc-0137-3d7d-8ae2-d6f6fb0d12fd | -3.58443 | -54.67005 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b77d0e9c-37c5-3a3a-80da-a371fdf5fec9 | -3.08387 | -54.25143 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39395416-f2da-3438-9d12-f90ea5646c59 | -6.2417 | -52.8504 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39d99538-744d-3b26-919b-ec1d498418c7 | -5.70527 | -53.49947 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5106a80-8f5a-3e20-85ea-6a8c3808bed3 | -1.09871 | -54.12514 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c129584f-0a5b-3ed0-ae8a-081a852794a5 | -3.05624 | -57.52198 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56bdc64b-8b15-30db-a31a-d67719b11143 | -3.35152 | -51.62552 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79f76f1b-6926-3e50-89c3-f9069f3cf15f | -4.23671 | -49.98626 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02f2436c-962c-36a6-a066-f242f247e942 | -2.21868 | -53.69898 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a5d48dd-c37f-311c-a988-36e9bde3f963 | -3.11674 | -53.76534 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a973585-7e05-3aa0-be90-f25ace3a278c | -3.13947 | -59.01334 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89cc45ec-438f-3aaa-98f4-ca7deebb68aa | -3.75596 | -59.46797 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d39ee85b-5df0-35a7-b38e-019dec132687 | -3.07572 | -54.25797 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e66b7160-3f19-3670-9bfd-43aecc268cdc | -3.57579 | -54.6802 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c6e1c3db-40cb-384a-80bc-8470d7a9f8bb | -4.69251 | -50.64279 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ff4f07-aa45-3bb3-a426-3bc4a44968a4 | -1.0993 | -54.12141 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4c307a0-2ad3-36f0-b592-3c0439b9fca0 | -3.52962 | -54.66594 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 978037f9-75c6-3bfd-9835-ce7a3075b5f8 | -3.11735 | -54.17402 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 760268c9-34f3-3cd2-8397-71e99ba7ad6e | -3.07401 | -54.24595 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3f40577-b3d8-3172-875c-42fe203f7d81 | -3.01381 | -54.23766 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cce951c-6fe6-3a65-9345-f0b60f8984ba | -2.99226 | -54.07663 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fa2ac816-99e8-3948-acff-440bb3ef3aa1 | -3.29855 | -54.03028 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2005846a-91f2-3a60-a714-0c9110fa712a | -2.9051 | -54.07914 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a001fcbc-8a2c-353f-b78c-c91316d4db09 | -3.16326 | -50.44674 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d143396-8892-3aa9-8ea7-b0c3c8090945 | -7.21182 | -55.16217 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73af08aa-bab6-3672-af1c-48ebe32ac7bd | -4.38001 | -55.16102 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7f64e0e-b9b0-344b-80db-33135666247b | -3.36182 | -58.18988 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39271782-8f03-33ac-ad7a-858d0a6312f8 | -2.48802 | -56.13676 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49bc39f9-fbc1-3553-ac5c-6bb3d750a144 | -3.09283 | -53.94033 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa2e97fe-56a8-349f-bd98-360e7e0c1435 | -4.26466 | -54.8755 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08705278-4c89-3faf-bfbb-d4a78f12831d | -6.88008 | -43.69935 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0410cc90-07e0-3757-84dd-2a03a4455060 | -7.21493 | -55.09546 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8b306e0-7678-3087-8769-de096459a1c7 | -2.97617 | -54.03853 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c22c5120-4a2e-3fcc-a365-12dfec6700e5 | -3.34652 | -50.47986 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 171ca360-afe9-3984-98f2-85bebc49c8e0 | -3.96049 | -56.11195 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 304a2321-f765-3fe0-a9f5-14e0c33594ed | -3.18187 | -58.83797 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f23ec13-cfbe-304f-a573-cac51e0a177e | -2.78091 | -54.06885 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b80abda0-cfb9-35b0-a3c3-f813d0820880 | -2.51837 | -57.24302 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d338bea-8cd4-3e1a-801e-d9af4cc37662 | -3.30022 | -54.04259 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10e344ef-b664-381a-b67e-3ed3640434e4 | -2.49619 | -56.06362 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0dbb7ed-ad64-3f8a-8888-b6736b574336 | -5.69478 | -53.49331 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d6fef79-724b-379c-bfb8-74280cc1b294 | -3.02795 | -54.07821 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb893e65-0d0b-3128-883f-0f36cd4d3c13 | -3.10097 | -54.18724 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cef37093-1bf7-34da-9a87-64fbe09dae1c | -3.00505 | -54.24802 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96145124-dbc1-3adc-9463-ca7507429443 | -7.20945 | -55.17751 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a01c0a-682d-3777-adbf-9ab6e5c6d15b | -3.28367 | -54.05608 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de2fadb-24d3-36f9-b756-2d4ca306a6ee | -3.00132 | -53.90223 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51f2eb2-45e4-3b8a-bf91-1a301fa59b28 | -3.07853 | -53.96227 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 44fdcc26-9c2a-3b2e-a47a-6a3361b92794 | -10.36714 | -61.21825 | 2026-10-08 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13e1e1ab-1e6b-3475-a290-f880d3708f25 | -3.56277 | -54.47857 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8858718d-2e3a-3a67-807b-2ad50f26766b | -9.2265 | -67.26945 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b0f7b50-4d6e-3457-b878-89db0f26563a | -1.29449 | -54.56339 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53174d8d-8ec0-35fb-a6ab-d1e4fe6a06fc | -1.50061 | -54.8273 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554b80db-1a60-35e5-90ad-a1065ebc5617 | -3.94651 | -56.04904 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 010f2973-fb84-39c5-9b62-164077ce1a1f | -9.26016 | -60.87664 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df8a5c96-e6a0-31a2-bf8d-6bb3e0d43e33 | -11.97926 | -57.57642 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77a9662a-323a-388c-83ca-05721fbb8095 | -6.93067 | -43.67394 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fc96259f-12d1-3d85-ab61-dbc39233cf04 | -3.29899 | -54.05041 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| efffc0db-8851-35f2-803a-29e960ecc3ca | -3.96794 | -56.12375 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f982158-3c6b-31ca-b7f5-67b32a63c856 | -3.53256 | -54.64729 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bce7c836-59e2-30fa-9d64-53df5a1ea5c6 | -3.26546 | -54.0572 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31faa2d6-fbf5-30cd-be7d-80136518951b | -3.04997 | -53.91352 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 352c9c0d-a4ae-3af9-ac36-c634d002dfe5 | -9.49266 | -64.3597 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a090ce-ed67-312c-ab01-91364efacdb5 | -6.67734 | -55.09922 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 056e4147-8122-3414-b0a6-149999358e18 | -3.51466 | -54.67128 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9700131-5836-3686-831c-5d381634c6f1 | -3.51364 | -54.63285 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a80184b5-f4ce-3ac6-b7b9-37d479fac679 | -1.718 | -55.44329 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8bbe979f-cf44-3244-a61f-7770812958eb | -3.05854 | -54.24837 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5464df8f-8e7f-36fb-b6ef-142e6ba26bc3 | -2.95893 | -54.17023 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d724250-14fc-3e2d-8bf0-0bf534403ced | -6.73616 | -55.11949 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4f13c42-fe4e-32e2-8c68-153a3f3c9a8a | -3.79287 | -59.32142 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e49c262-6491-33e1-9fec-b7d728a8ea6d | -3.17589 | -50.59574 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b3a9a1ca-b259-3277-afe3-84f2dfe4dec8 | -2.98696 | -54.08389 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7c619c50-1701-3fe0-ae6b-d062233da070 | -3.54194 | -59.50912 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd1ae5e0-972c-3b25-aa22-5727eed43b56 | -2.76281 | -54.11028 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83a51e7e-a2a4-3129-819d-0376678d063f | -6.09501 | -53.49586 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90dbb303-41b6-36a1-a86b-79fb88813935 | -3.58718 | -55.56124 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372b5b3d-de90-381c-be75-b602f5fc91d2 | -2.93391 | -53.94003 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80c8f577-007e-3cd5-bf55-b55c39abb802 | -2.86565 | -54.19515 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c082ef0f-e7f0-380a-a420-21ac133dde64 | -3.17556 | -54.6086 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f778eb6-1b11-3704-ad48-3ab9498a19b8 | -7.27831 | -46.80523 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99d3e000-064e-37f8-8550-5a1bab1eb02a | -3.28031 | -54.03151 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ce0bc7b-fdb3-3301-b23d-599c02035d25 | -3.57637 | -54.67646 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8d7c46b0-d68d-3845-a856-caba67526ab7 | -2.15776 | -59.224 | 2026-10-08 05:23:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e3e98d-49c3-30e5-b407-60dcc3844c2e | -3.2711 | -54.68744 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4fc84bd-354e-3f78-b57a-4805c86ed742 | -2.77383 | -54.09145 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5434d413-8ae9-3aaf-83e5-fdae71d8446a | -2.79022 | -54.0782 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README140.md)
