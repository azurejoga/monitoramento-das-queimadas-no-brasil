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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff7edf9-2ad7-317d-aec9-1a692d9470f6 | -3.0289 | -54.070301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f792fb8-7215-336c-98c2-53940c59c697 | -1.5012 | -54.8358 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 791319ba-d663-3c59-9e98-a81b84ee1766 | -3.3218 | -50.1758 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0d364a8-93a3-33bd-899c-560ea4a181d9 | -4.4498 | -54.974499 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65521b93-cb3b-3f20-a832-0460a019227b | -11.7811 | -46.775299 | 2026-10-08 00:26:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2b59a09-5ddf-3c90-9ec2-c4262b0a4119 | -4.1226 | -54.028599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45560998-0d4a-3937-a68b-a0b896caf108 | -2.4015 | -57.229198 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87d88cd1-a949-3722-b2bb-38a877e608e1 | -3.0481 | -53.9277 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c584436-9e3f-386a-b578-d77356d405e5 | -3.0985 | -54.286301 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe195305-9d2c-33c4-afcf-bee2595eb85e | -6.2235 | -52.6562 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2107a68e-084d-3314-9820-4913505146ae | -5.7189 | -45.128601 | 2026-10-08 00:26:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f46e451-6628-31cf-92bc-32e335d30234 | -3.3628 | -50.486301 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18f4a841-585d-3e3d-b71e-cec5b97c0a3e | -4.8168 | -54.727901 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a538fd-f97a-3ef7-a8b1-9fd38124cade | -3.0093 | -54.074699 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ed6637-d885-32e8-8119-169c83a93fdf | -3.863 | -50.4221 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f642f8-6757-3c2b-8fdc-1600324af930 | -1.8228 | -54.9361 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2f0c1f-f1d0-3e18-b17c-8a4cb5f85c00 | -4.368 | -54.749001 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 796e47c9-71d7-35c2-9746-bab05f981d1b | -8.7124 | -45.183498 | 2026-10-08 00:26:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07a036e3-c918-3485-a9fc-a8bb862b1f66 | -3.0933 | -53.763699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6845774-f7f8-34c6-ab25-af77c052f572 | -3.5312 | -54.649101 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 336eae47-82c8-36e3-b852-3324ded4a47f | -2.7529 | -54.0811 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66518282-2cd8-3250-aa82-433c3876c8ca | -2.7627 | -54.078899 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af2d813a-afa8-37f3-b382-35c7f98ad289 | -3.353 | -50.488602 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e31ebc8-22a6-3bbf-9d83-adb1a68cbf2d | -5.6878 | -53.474201 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d457e30-e5a2-3971-802c-2b1e62f82d1d | -3.2691 | -54.038399 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e9c49a-dce1-3fac-b4f2-52c912c92dff | -3.2247 | -53.888199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5cde879-d42f-30b9-9744-0356e571ef5b | -3.5423 | -55.521198 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273ca167-204c-3d18-9716-5e5b4581df3a | -20.7318 | -48.978901 | 2026-10-08 00:26:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c06eaa6-d429-35a8-b50a-16d8a25cfc0a | -6.6134 | -43.734699 | 2026-10-08 00:26:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c194c99a-3a27-3b5a-9735-f2c148ca2f7f | -2.3818 | -56.133701 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9994c039-29c2-34fe-af41-865508ababd2 | -4.1211 | -54.021702 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41dd5740-bd8b-3993-b4c2-e4706a47d72f | -2.3626 | -48.8783 | 2026-10-08 00:26:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92a6f672-141c-33f1-b074-8d896de44115 | -4.307 | -54.798401 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 152e3fdd-22c1-358e-90a7-804e3bd78097 | -10.436 | -47.271702 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9b30e8-e1a2-36ac-afc8-ad4a50a7e61f | -3.5877 | -54.306702 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905f76f6-cd12-35ac-92aa-0e855f14ffb6 | -3.178 | -58.631199 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4617f4-93ba-3d37-94ff-5909925e2c98 | -3.669 | -60.617401 | 2026-10-08 00:26:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9fe1641-a9e4-3a40-9849-b3d4bf7f48c9 | -3.0028 | -54.228199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db5c7143-5ad1-37fd-b851-e8b7b0e11c57 | -5.8609 | -53.464401 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3bf6da8-7698-36c2-8b49-2598feb2a752 | -7.8772 | -54.961899 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349c5f92-cf45-32ea-ba65-02ce0ad5a0c3 | -2.8913 | -59.1898 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb5a524-c2f6-3875-8ef4-30fdfd661784 | -2.9256 | -54.115101 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b549bd9-f819-3f3c-8a57-71cf556da802 | -2.4624 | -56.079399 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c915c2d-802c-35c8-8fd3-0882d8657559 | -11.0624 | -49.533501 | 2026-10-08 00:26:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c45f2f5a-9782-357a-9ee0-63a6451a8a64 | -4.3061 | -50.778099 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9e6291-8104-36be-913c-14a41e33fb2b | -3.0635 | -59.2715 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6117dc5-487f-30e2-a145-3c2f07cc9cac | -4.9666 | -55.1189 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6758fc-3f83-3222-b7fe-c52eaad79168 | -3.2887 | -54.034 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a95223b0-cefa-3d5c-89ee-3e9d83a7acc3 | -1.4744 | -54.762901 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4889db0e-b56e-3fc0-9b69-ee8b23417ca1 | -2.5726 | -56.157299 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5395d14-891e-3358-8238-ca2c2ff8a3f4 | -1.9984 | -56.947701 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 118c8840-0634-3b4d-b193-a791deca0f0d | -3.1642 | -58.6157 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22ffc378-973b-3dbf-a7bd-90f66a69651c | -2.3922 | -57.875999 | 2026-10-08 00:26:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79c853ec-3390-3d2f-8156-433c6248ae1f | -1.7973 | -57.106701 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 142d8d75-deaf-3a8c-8755-4f4f0cafaebf | -3.5714 | -59.4785 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb3801d4-10f8-3dba-bc17-708d1c78ca19 | -5.0843 | -49.6945 | 2026-10-08 00:26:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dfc8439-3e94-3577-86a9-9d5191507d6d | -3.0202 | -53.9412 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3cbb0f-314d-3b0e-93e7-699bbdb8c009 | -3.5569 | -54.672001 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee0d70b-2872-35ff-8709-10530d1a69a4 | -3.1713 | -53.834301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 546ad42e-63d7-39f0-bbed-2d03f5b311a0 | -2.4976 | -56.1446 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84458549-0255-3048-92d6-7bba4c0f6e4b | -10.433 | -47.259602 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e01cee7-5c9b-3e1c-85bf-f14d168ff2ce | -3.0213 | -54.173401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536908ac-8101-35c3-9805-92cf79221dc1 | -6.2413 | -52.869999 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a2dbe43-89f1-3cfe-af1a-020e2bfeac84 | -7.2209 | -55.159 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11588f6d-d4f9-35e9-992d-695750cd177b | -7.2057 | -45.370899 | 2026-10-08 00:26:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eba540d-2019-3a8d-8c9f-5153249b4abe | -0.8438 | -51.849602 | 2026-10-08 00:26:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 116b4031-780a-3a34-9f28-3e1a646178db | -2.9484 | -54.124599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0650fff0-3ff6-3726-967c-38c5bd53f6fe | -22.020399 | -49.5644 | 2026-10-08 00:26:00 | METOP-B | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 830bda5f-7749-3701-ae10-68f406a85eaa | -4.1797 | -59.3993 | 2026-10-08 00:26:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ced29054-43cb-3a04-ad85-7ae8c4217a92 | -3.5978 | -54.670101 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce5b3a0-8080-3873-9bdd-cece6ab8aa58 | -2.7741 | -54.083599 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d524d9c-0bd9-32ae-b29c-6932ab3b8396 | -2.0282 | -56.759602 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3b7513a-2b4b-38fd-ba3b-b41bbbb02d84 | -1.5095 | -54.8269 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56bf942f-a3bf-32e9-8f74-f76a6347bca9 | -3.0073 | -54.111401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 564635a8-1bc0-3582-a245-9e026fcfe32b | -3.0575 | -54.151001 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b69462-ad96-3a86-b72d-e3bb3503e523 | -1.4646 | -54.765099 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f4ef0f-a9de-345c-bcdb-5a9042521521 | -2.8762 | -54.169701 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb0e5b3-e9df-3606-aec6-53c28dc41b81 | -14.2361 | -48.534302 | 2026-10-08 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc87242-28de-3609-9da3-872e5b470222 | -5.8791 | -50.095402 | 2026-10-08 00:26:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a741c8-b2c3-3d8e-99c4-2b51a9af1b71 | -2.2531 | -51.932301 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832b3581-3e1a-3981-b030-53f6d6098ae1 | -4.304 | -50.7691 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734c6ab4-e6ee-3a27-9837-90be139ff9eb | -3.0094 | -54.758099 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0706dcfa-0f25-3a28-b233-5f2779e8bb39 | -3.0421 | -54.219501 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aa31d1a-4dd2-3861-be98-88bc562b0f15 | -1.4867 | -54.5443 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3533971c-b33c-3588-afdc-eb5c97482f95 | -6.1151 | -51.7342 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ff27b3-f1c2-358d-9c4e-371a1e103f7c | -3.5675 | -54.354301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b428b25-4dcd-34cf-baa2-27b25f7897cc | -5.9512 | -55.3297 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 448feaaf-0db6-37f8-991f-3c7fd226396e | -10.9704 | -45.389599 | 2026-10-08 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c54d45d-68ac-3127-93a0-dc2b467d975b | -4.0621 | -55.312199 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c769cef-e085-3e29-b5f2-85fc7287d335 | -4.5495 | -54.959499 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1faffdf-09e8-3e54-8165-75c62b654674 | -3.8754 | -55.994499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04ca1774-051a-3da9-b58f-18c61a071cd7 | -7.4352 | -55.5681 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c9f9b1-2684-3292-9cf1-8924f22517a2 | -6.105 | -55.695702 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19230452-a765-33b7-90b8-9fd8dd4192f2 | -3.016 | -54.058601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0118342c-c9de-3d7d-bb8e-e06177bfab1c | -2.3428 | -55.6861 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1ba99e-4da6-3532-b24e-8843adcffa1e | -6.4885 | -55.291698 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee7e4bac-849b-3d57-bb01-124c2b6afafa | -3.5794 | -54.3158 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee78218-c6c9-3983-9f17-dd07ef1be22e | -3.0046 | -54.053902 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22908679-6d06-3574-a769-bc017701359a | -2.8844 | -54.160599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5bf1ce0-d8f3-32a3-bcde-c7b0d1aaad72 | -3.0402 | -53.893002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
