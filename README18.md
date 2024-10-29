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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab5328ac-b5dc-357d-81b7-f4edc5cc1728 | -3.47366 | -54.57447 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 27f1b078-e926-3e0c-9181-ab9601f26720 | -3.46027 | -54.62201 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| cda11fb4-4d62-39aa-ac2a-6322c59b332d | -3.44041 | -54.26532 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b8e8dd57-7865-370e-b101-7ad5e0e67828 | -3.43893 | -54.25961 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5ec0c4e5-3af1-387b-ab5a-fa1a05e42ade | -3.41135 | -54.49184 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ba0d570a-4fc4-376c-9020-5d818c1d1926 | -3.28931 | -54.71546 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cced273f-2512-388a-8382-403cff0cb706 | -3.27344 | -54.17537 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7d7a672b-beda-3357-bba5-e9af3ec719fd | -3.26328 | -54.17695 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3b8355b9-a009-355f-ad94-3afa46c9d467 | -3.13541 | -54.28052 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e1f27b16-6dd7-3c28-a213-255e3bb0cec6 | -3.13373 | -54.26865 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 76bf767a-cc07-33c9-83a6-6209c2a8ac85 | -3.1253 | -54.28205 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| a8612ce1-71a3-3763-81c7-0f82815f5c24 | -3.12362 | -54.27025 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 012906ae-0e70-3517-95cb-fb528e248fec | -3.11687 | -54.29527 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c4e76d7d-f799-3238-aa54-97cb781ba572 | -3.11519 | -54.28352 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4b3cbe89-7bd4-3506-b137-7846eca960cd | -3.10676 | -54.29673 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f85c7dbc-e311-3552-959c-1a37d22449da | -3.10507 | -54.28498 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 199.8 |
| b7f89349-7075-3121-bf10-c4a3d330fa13 | -3.10337 | -54.27322 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 17638f85-1164-3faf-89fb-65593b515d5e | -3.09665 | -54.29819 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99d16b87-0a9f-3ca9-a8fe-52f5f1f88c39 | -3.09495 | -54.28645 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 08b08028-4efb-3bd9-8785-f2202ff37ef4 | -3.07945 | -54.17977 | 2024-10-29 01:30:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f2ea58a5-666f-31e7-bf8e-40508c0eb825 | -3.07769 | -54.16767 | 2024-10-29 01:30:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| bb636a97-4a2c-3a9e-919e-a6c3317ba2ed | -3.06749 | -54.16924 | 2024-10-29 01:30:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8fe28416-dd2e-37ce-8f52-9699ffa7a9ac | -2.97625 | -54.52777 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5769fb7c-23b9-3a3a-9655-aed2fe063376 | -2.97463 | -54.51642 | 2024-10-29 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| c8f35ac0-5cec-3bd2-bda4-a4402fbec0fb | -3.59701 | -53.79351 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 367eff5c-81a3-3a86-bc4b-e57013ec34de | -3.59521 | -53.78112 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| e2bb2f8f-c4ef-3228-88ad-01599a14bddb | -3.10565 | -53.72741 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6612e8f3-5ed0-3f01-bd9c-71fa6b420eab | -3.10377 | -53.71457 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d358ad87-8a88-393e-b521-a1098c73576b | -3.09762 | -53.81885 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a718e10-5259-3354-a272-2c9c94e9db2e | -3.09579 | -53.80641 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9c5542ff-a9a3-364d-9b7c-5a767deea2a9 | -3.09322 | -53.71608 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 869dd939-da17-3bd7-be48-9811dd562a99 | -3.09026 | -53.81331 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 643978e4-c51a-3ec9-ac82-203d4e113c9d | -4.34225 | -55.131 | 2024-10-29 01:30:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fe318fc0-1b5a-39b1-89e0-e7bb670d254b | -3.98344 | -54.13237 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cd2c3db7-7174-3a69-bbd3-cb05361f633e | -3.92515 | -54.51254 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63666602-d838-35e2-a51f-246851829f23 | -3.70923 | -54.43049 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e38b40a6-0c79-3695-994f-96924d06e415 | -3.69487 | -54.25782 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f8059b3a-073a-3339-97f3-9da6313bb3e4 | -3.673 | -54.3197 | 2024-10-29 01:30:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 94d92204-e1a5-3450-b552-54211fa19291 | -4.10124 | -53.95149 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3b777ff1-4718-33eb-9018-7339707682e5 | -4.09951 | -53.93946 | 2024-10-29 01:30:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 414e753e-1b3f-305b-821b-2dfe0f4dd983 | -6.55766 | -54.95549 | 2024-10-29 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f7404237-ea75-3417-98db-c4fd7e65b554 | -4.73226 | -56.05785 | 2024-10-29 01:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cc47692f-08b3-37ed-a500-0873fa294940 | -4.73095 | -56.0486 | 2024-10-29 01:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| aaade25e-69a4-3b3c-9ff6-feb76dc5d898 | -4.38646 | -55.75988 | 2024-10-29 01:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8873cede-8cce-328e-a59d-cf62d8f60007 | -4.09932 | -55.49841 | 2024-10-29 01:30:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6ac05fea-1b49-3faf-b1d2-0795ad52d716 | -6.26516 | -56.53184 | 2024-10-29 01:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c626ec23-68e4-31be-8fa6-d4e9cfd98496 | -6.26391 | -56.52297 | 2024-10-29 01:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eac4f6d4-135c-31ca-b8a0-d0f109561a2d | -5.30897 | -55.83377 | 2024-10-29 01:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c78e6b50-b810-361a-80d6-4907cb532a8b | -3.5506 | -58.68486 | 2024-10-29 01:30:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 03b1e94b-9810-3155-9d2d-4c0ddc52738a | -3.54934 | -58.67577 | 2024-10-29 01:30:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ec077fd9-41b6-36b0-b0a3-ef75ab437f4c | 3.57845 | -51.27654 | 2024-10-29 01:32:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 30.8 |
| e4282b32-98eb-38d0-a549-0c52a01c0bc7 | 3.57623 | -51.27061 | 2024-10-29 01:32:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a4515bde-f939-3112-b73d-52429636bd7a | 3.57273 | -51.29631 | 2024-10-29 01:32:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 24d227f2-248d-31c1-8647-770a1d98c20b | 3.45835 | -51.24802 | 2024-10-29 01:32:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8922c72c-97b0-30a3-acb9-01c77976eae1 | 3.4549 | -51.27373 | 2024-10-29 01:32:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.3 |
| caabe8d2-bfee-317f-a925-4b91838690f8 | -1.08212 | -53.17383 | 2024-10-29 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5104213b-4d91-3a28-95e4-c157c8a7af88 | -1.08019 | -53.16843 | 2024-10-29 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 482f498f-e91a-3175-a7c7-49db4ba04492 | -1.98165 | -52.08087 | 2024-10-29 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 657f24b6-0f1f-3fdc-9fff-97b307ff2136 | -1.54093 | -52.1208 | 2024-10-29 01:32:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e136d038-13ca-373d-977f-c9503ce3dca9 | -2.20184 | -53.69225 | 2024-10-29 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 62af9aff-55ae-398e-ae46-5e85256fe963 | -1.7476 | -54.45069 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 685cc00b-ae45-31f9-80ce-b83bffe6510e | -1.74589 | -54.43871 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ae520e06-ced9-39a1-8f28-c18f9c1b5d15 | -1.71922 | -54.53405 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 68f88be0-3753-3291-8d72-93f50ca75d79 | -1.71757 | -54.52221 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 64f65c08-ab0c-331d-a9a1-a4c5426ee754 | -1.70907 | -54.53556 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a0ab80e9-bfd1-37ae-add4-d84938ced144 | -1.70741 | -54.52372 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fb8fba0f-c225-3c62-b829-d53520fa9ac4 | -1.56383 | -54.45291 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 268852b8-e2d1-3a63-9c3a-605594d29007 | -1.42907 | -54.22936 | 2024-10-29 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 3218fa69-023d-32bc-95d6-e2bdb75f2cc3 | -1.4187 | -54.23126 | 2024-10-29 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4fff4ac7-9306-3115-a0c9-eb4d77beb146 | -1.39089 | -54.03934 | 2024-10-29 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6d7d7609-7b60-37bb-85f1-c506754f6e76 | -1.34182 | -54.61554 | 2024-10-29 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ea3c2368-6c57-3102-a7dd-a88a8b81616b | -1.33665 | -54.65231 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1af3166b-d5a8-392a-8c57-f0f1f4f7dd15 | -1.20965 | -54.17637 | 2024-10-29 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 843502b1-b06d-3f55-b316-4639236b5d9b | -1.17811 | -54.18068 | 2024-10-29 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 08d8118c-6e49-31bc-bfca-db73d1d76070 | -1.0829 | -53.6653 | 2024-10-29 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| cb2f5662-35d1-3d8c-9122-2b8099ecbfa5 | -1.07198 | -53.667 | 2024-10-29 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5df797df-b5fc-37fd-9551-214db3a9dfc1 | -0.98686 | -53.71483 | 2024-10-29 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| e01dfa50-8bee-38e2-a780-a46688b315bf | -0.98485 | -53.70086 | 2024-10-29 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3f3f8de9-b673-3e65-9bc2-294362ec201b | -0.97606 | -53.71714 | 2024-10-29 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 9fb9de48-7db4-3214-ac64-5bd9721490af | -2.83009 | -54.22142 | 2024-10-29 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7b70d10c-3fb1-330a-a29f-abe06fc207a4 | -2.82836 | -54.20935 | 2024-10-29 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| babac6d9-3b38-3668-ad77-e0a3ca1f7352 | -2.78208 | -54.74047 | 2024-10-29 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 38ef2806-e13d-3aff-b056-1b1a0be40711 | -2.78047 | -54.72932 | 2024-10-29 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 0abbb03a-92e3-30cf-a1d0-4f15268729b7 | -2.56692 | -54.01657 | 2024-10-29 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 644336d0-f790-3435-b76f-ad1154dd3a63 | -2.55652 | -54.0181 | 2024-10-29 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c98eaa45-bbce-3e99-807e-63c0d5fd64d0 | -2.27429 | -53.78381 | 2024-10-29 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8cec6c5e-1c05-382e-a957-74c755c2e31e | -2.25035 | -53.72604 | 2024-10-29 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2532c454-f6b1-32ad-9d4b-e8dd565d879f | -2.12653 | -54.81503 | 2024-10-29 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 233aee9a-c254-34f7-9fb2-4443928b5dc9 | -2.12496 | -54.8038 | 2024-10-29 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b258c66d-f43c-3fb6-89c0-5454e7b00ba7 | -1.99975 | -55.70839 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7b71140d-c1c8-3a60-9181-b81d8ec67c66 | -1.80566 | -55.70752 | 2024-10-29 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 325e35b2-d65f-32c4-b6d9-cd3e114da9f9 | -1.76895 | -55.55269 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b2d23a29-85a2-3f42-881b-1d68e64aa78b | -1.75651 | -55.22809 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 82a2b674-a16a-32d0-bb31-528e9203c25a | -1.39975 | -55.37946 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 96e61ec0-ef3e-335f-8ccd-9a67b58e6f72 | -1.3763 | -55.86035 | 2024-10-29 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9d4c0903-e46e-32aa-87c1-7f6a6180dad2 | -1.36691 | -55.86164 | 2024-10-29 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 69780199-d222-36b7-9ab9-e44382f6507d | -1.36131 | -55.68739 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 109851e3-9b0f-38f4-b239-f2058eb04104 | -1.34497 | -55.15173 | 2024-10-29 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 48d3787f-b31d-3c13-8674-7afe52d55a75 | -1.2951 | -55.73433 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e5832eae-d505-3d0f-b4a1-2914ba94fba8 | -1.29367 | -55.72416 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |


[Clique aqui para ver as próximas entradas](README19.md)
