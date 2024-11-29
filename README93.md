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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 300ec38f-5fbd-38e8-9739-597ffb8e4276 | -3.47403 | -50.53812 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79e3ccba-f16c-3318-92c5-059c4bf35b5e | -3.11264 | -53.7573 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83c5e7f1-30a7-35be-ae0a-88d8621e9d17 | -3.23663 | -54.22181 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ffd84c-64c1-3b79-830e-311fe5e1834c | -3.41169 | -54.17586 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcade603-8abb-3a39-8731-f1035712fab5 | -3.33621 | -53.21806 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dff7e04f-ad4e-3644-8c56-ff237e5d2c4b | -2.98218 | -53.8925 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de3cfb0c-70f8-37b0-b5df-0c6bf048289e | -1.70833 | -52.76572 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 826b8a7f-810e-3f1c-82b8-bb564ad1ec14 | -2.84854 | -54.02856 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25337280-e8b7-3f01-8e3a-88cf4f1b90c9 | -3.49753 | -50.4595 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 535cfcc9-11a7-3ee9-bbd5-fe42113bc6ee | -2.34454 | -53.91484 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3413b41-4c19-38e4-b49f-95d37212ab99 | -3.89636 | -49.81709 | 2024-11-29 05:22:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3e8759f-15aa-3bc7-8d2b-3cb8673d7025 | -2.62008 | -51.75856 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2793b7-0ecb-31d8-881e-d0c15d994cc2 | -1.94941 | -52.96912 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec241c81-d17d-38be-b079-4afe388ccee3 | -2.5826 | -54.24231 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99101c9d-21b3-32a9-8b21-a25bd1157b81 | -1.5353 | -55.86361 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb3d6261-f06c-3e1f-9eee-07894140744c | -3.59621 | -50.3592 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60faa0f-778d-3b3d-b83f-54e634d85f33 | -3.4987 | -53.804 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 985a37d2-3d0d-30c5-9131-14600862b887 | -3.53149 | -50.19575 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef2aef7d-520a-3bf5-be2d-5dab3ee7f87b | -1.45682 | -54.51693 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d8d0862-0f61-3387-9dfd-f516b9db71b7 | -1.65294 | -52.73403 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c93d357-a8bd-3b7c-b755-2be759879624 | -1.60308 | -55.42678 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3de8d3f8-1aa2-31d0-8068-582131f3c235 | -3.70852 | -50.51405 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef892397-bb45-33a4-810e-e2bcf146a2df | -2.8323 | -54.10495 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 664adda1-1872-3cfd-93e2-ebf4413123da | -2.84431 | -54.02797 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e24bf382-ba31-37ae-8c55-8f09cd0798b8 | -1.34894 | -55.02639 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5bf6ec6-6c7c-3bfc-975e-e500fc694b40 | -4.20075 | -50.68502 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12d44bcb-1988-353c-a882-3680a92ffbb3 | -2.65109 | -48.78098 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 490554ac-9261-3d26-8497-f16c4d9d1027 | -2.01201 | -55.39909 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dc2bc4e-42ba-388c-9238-82501c01fabd | -3.41306 | -50.15836 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d73eb5-8f72-31e5-a195-16edf9666a60 | -2.87766 | -46.86359 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097bc387-5700-3755-a175-9ffa2f9be854 | -1.38165 | -55.68274 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29c24ea6-526e-3f1b-80fa-7e4937259e05 | -3.10492 | -53.80933 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a2ab541c-9b0c-37d0-8af9-8ab506063e1c | -3.47507 | -50.53124 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3467618b-51fb-353d-8e4a-2b0e7f2a49c4 | -5.18368 | -60.26482 | 2024-11-29 05:22:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d599cd6-0f75-360a-913e-9b3828104a09 | -2.75389 | -54.11246 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa437f7c-6b18-315d-a0f0-dc7132c6d5c5 | -2.233 | -53.69129 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2637d31-6769-3ae8-90cf-026be82bd6e8 | -12.41479 | -63.71468 | 2024-11-29 05:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f692dd3-a915-3664-9d67-511f755d9158 | -2.5725 | -49.99683 | 2024-11-29 05:22:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64843b0a-d3e4-35d7-9192-79e56beb7c31 | -2.06049 | -56.08075 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a83461b-0515-325d-905d-3773364a0b9e | -3.26259 | -49.89515 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d93fb5c9-8bab-351d-8c66-c9716bbd5063 | -3.70785 | -50.51487 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7cc57c3-7a5e-3b18-ba26-71682cb3b87a | -3.49377 | -53.8073 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcca09b0-2e5c-39d7-bf6b-c09839a682cc | -2.84013 | -54.11401 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bc4099b-98a7-3fb5-8d07-dc67da15bb6e | -2.05314 | -56.07962 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2bc02b3d-303e-31d3-88f1-58acd0db7771 | -1.37766 | -55.04533 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71392194-5b6a-3f40-92c0-36b082ef6b51 | -4.42803 | -46.57882 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d64fecc-4258-3e4d-a598-a2ed5c1358bd | -2.7043 | -49.83466 | 2024-11-29 05:22:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc1666d3-6f0e-3137-9f30-96f620e4345f | -3.25892 | -51.21311 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c6fd69d-9f71-3474-a243-ceec4cab3d8b | -2.96088 | -53.88899 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85b8c42b-6b24-3baa-a757-3e9814d81a70 | -12.10347 | -58.23952 | 2024-11-29 05:22:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c573192f-9dac-344e-8ddd-7dcdcbdbaf4c | -1.99214 | -52.09784 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a1754bd-49d0-3bb8-97d7-6984f678f51c | -2.29184 | -51.98552 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ba6104-b573-3ac5-bc5a-23c779376bf5 | -1.88914 | -54.5388 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1faa4869-9b62-3ac0-8714-eeecc9d2397b | -3.18649 | -54.3258 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8431aef-1893-34ca-bb94-4ad5d3337486 | -1.98942 | -53.29615 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68fb9b04-3bf1-36f8-9e3a-8a206b3fc9de | -3.54426 | -50.18643 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d4e7d5d-5909-3f51-bf84-39dd48ac5ec6 | -1.67959 | -52.53225 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e357630c-f0cc-35f3-bcb6-494c7a6d1e6f | -1.46083 | -54.5175 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86e4a13a-8b7c-38a9-b61a-238e164d71a2 | -3.41747 | -54.90589 | 2024-11-29 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7402cc0-d91d-3a4b-9098-9f0408c45028 | -1.72353 | -52.4842 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f8088ccc-8854-33ac-9ab8-0a1161a4b397 | -2.29767 | -51.98516 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0962b51-7442-3095-9161-53d9bf4fbf87 | -1.35099 | -54.98769 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5950927b-f603-301d-a89f-849fe6880955 | -3.48718 | -54.6673 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7a1b06d-9543-3747-af2d-f544c843a233 | -1.63303 | -53.86483 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97824f23-0d30-30d7-80bd-5ba43fd4feec | -3.47024 | -50.53329 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a988fe58-06c7-3913-a2da-8981c332388e | -1.64237 | -52.73853 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1af188aa-a74f-3765-b76b-4deac83b2c42 | -1.70002 | -52.63828 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3e1cfd50-00f3-39b2-b24f-d01a6dc91178 | -2.7608 | -54.06664 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc337563-cff3-3b9f-83bb-8ac3673387a6 | -3.67296 | -54.44612 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d75533ec-9bac-36e3-bec1-bf5ef2f1caa0 | -2.98021 | -53.29221 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a22fdde7-6efc-30a1-87b7-6af4dcf2d94b | -2.5052 | -54.16466 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf795986-bb44-3881-9fda-b86b8da75fc2 | -1.8834 | -52.66084 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb1b74ba-72b7-3385-896c-95fb675640dd | -3.89779 | -49.81775 | 2024-11-29 05:22:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97495c11-4752-3bc7-9a98-8507f04c832d | -3.39534 | -54.28414 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0051258c-5f91-32d2-b687-6038b92107b3 | -2.95665 | -53.88814 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50bc6382-7808-3f81-8fc2-77645c345754 | -3.10203 | -53.25483 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49e43a6d-b825-307f-a6e2-241e704eda93 | -2.97578 | -53.2914 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 037398db-532c-3ba9-a184-13ebe1d166fa | -2.84052 | -46.82088 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b34b906-24cb-3fa6-957b-57cd69fca6ba | -2.80385 | -51.59 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3023a43-86f7-39a2-868a-65cec40559da | -3.38307 | -53.50369 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2ffec1-ea0c-3e81-b337-a40b625e7a17 | -3.96471 | -50.19017 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b1fd451-6b8c-3742-8b57-50ad33a4fa8d | -3.02596 | -54.02262 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 630529e8-ea69-3e90-b870-2d4ea707bcbe | -3.78633 | -50.13243 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8ea545-7980-3d85-9a5a-13fd0a7a0cc1 | -1.62823 | -53.86811 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cba15fc-b604-3bba-b5bd-0b3e6c040271 | -3.17819 | -54.32447 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6122bfe5-2c65-3754-b684-fc8a19123bc9 | -2.83531 | -54.11321 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c1d6adb-06bf-3338-adb3-b925c8b3b9f6 | -3.04894 | -54.04205 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bec1b30-c7d1-3318-8d0e-6657f2bb0753 | -2.05381 | -56.07534 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd75d4db-378e-3efc-90cc-bc31607657a0 | -2.69818 | -51.68074 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9857962-862d-3503-8cce-40815247eed2 | -3.24289 | -53.63174 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74781345-2103-303a-9f00-3d8958a4fee6 | -1.99767 | -52.09352 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7363cdd-c966-3206-8160-f0fc9a1c7d2e | -2.89813 | -51.57525 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba65bab3-b8ba-30ef-bdf6-a6b7a4f19682 | -2.84913 | -54.02473 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84ca3fd1-d99f-3053-bf43-a72ec755085d | -2.16735 | -53.27862 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d83f1e12-ebf4-3b75-859a-002a5c58d1f2 | -4.08349 | -47.03127 | 2024-11-29 05:22:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f156b124-bfdb-372e-bdd8-8bc7b2681008 | -1.58001 | -53.84202 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ee507455-d026-3a83-87cc-6a0ca4ef5035 | -1.6948 | -52.4555 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 278c0e7b-1aa4-3e7d-a4ce-cf8bc751af90 | -1.66722 | -52.73158 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1749662a-baa8-31f6-8c48-f22f67bcb258 | -3.12987 | -49.40681 | 2024-11-29 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 408e2eb8-93a8-3297-92ac-e1de9f32148c | -3.3758 | -50.82799 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README94.md)
