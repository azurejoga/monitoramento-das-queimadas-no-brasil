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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c668b6de-148c-31b4-84cf-e9217b53a6b7 | -10.99516 | -63.57619 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 382a728f-0aa0-386b-89d7-65f106e88a5e | -10.99448 | -63.5796 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a4b5536-8d28-3d51-8b19-71edc2247107 | -10.99438 | -63.57774 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2824fd1d-cb21-33b0-ac2a-b51efa016d19 | -10.98895 | -63.57558 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6af5dcad-59a2-3ab6-982e-324f45c2a94c | -10.98818 | -63.57713 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4c9501c-5f27-3cce-ad1b-bb3f6d8729f8 | -10.9859 | -63.94377 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9efbfe70-c850-3f8a-93d2-3a68da75201e | -10.98489 | -63.94886 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0522b18-07e6-3eb5-9ac7-24848fafd1ed | -10.98339 | -63.57175 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9103276-0e41-333c-a877-461b60433ed7 | -10.98274 | -63.57499 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78c2a384-47f8-3983-9212-5c9b27a0ab00 | -10.98259 | -63.57336 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 26fce308-84d3-387d-a936-0e16226f38c4 | -10.98196 | -63.57658 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cbe7024-8808-360c-835a-87248be46fb5 | -10.97643 | -63.57487 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35126afa-2d12-3b8e-b1de-848abc8d3911 | -10.97631 | -63.5731 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c8d7b9e-1f02-370a-9395-595217d27975 | -10.8702 | -63.88505 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eefe8991-2235-3f52-819e-6cf9535342dd | -9.29686 | -65.34165 | 2024-10-02 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0f374e3-7787-365d-a4a2-47be61674b43 | -9.29548 | -65.34858 | 2024-10-02 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8dd04e80-93a0-3527-8a26-11ded2be6bc9 | -9.98844 | -64.77104 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34772b00-82da-3b9e-a425-8ff36b57d1a6 | -9.98178 | -64.76981 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79ac2646-e6c9-3404-be9f-4d3fcd241b91 | -9.97068 | -64.77509 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2fadb1d-8fbe-3938-a7a5-2b3c0fb1bcb0 | -9.9695 | -64.78087 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb00e709-5ec8-3813-9f2c-2f62106ea4e5 | -9.9673 | -64.77313 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9228daf2-267c-35cd-bbd7-4074989d7059 | -9.96616 | -64.77893 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b86680f-2409-3566-9190-9e17de4224c6 | -9.96404 | -64.77374 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 214debdd-12dd-30ee-bee2-4165d3418a3d | -9.96285 | -64.77953 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1db8cd9-23ac-38ee-8b90-912efd644067 | -9.95156 | -64.90248 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b969f01b-b8e3-315d-9e97-300164ca4c12 | -9.95031 | -64.90861 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d4a43fd9-97b3-39f4-84a3-80536b373d9f | -9.94904 | -64.9148 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c6f2685d-05fc-33ad-8d30-3fc94d4550d0 | -9.94897 | -64.90083 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 22c140f6-c5ed-3753-a481-4f40e695a948 | -9.94777 | -64.90693 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 40de43e7-de7f-38cf-8d38-4e4948ffe4e1 | -9.94776 | -64.92108 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5c6bfc80-0508-381e-9062-baf2f53069f3 | -9.94656 | -64.91305 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 966ffb4f-4e76-3005-858d-26e842cd7900 | -9.94531 | -64.91933 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e20d5fb7-55b7-369a-8818-a845dd1bb07f | -9.94486 | -64.90119 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d4de8e73-1628-3b48-853f-92f8bcee6fcd | -9.94361 | -64.90726 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8fa2f117-ad27-36d3-977a-b2317bcb359a | -9.94236 | -64.91337 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d0f95392-ef6f-355c-b3b8-007edc8df8d5 | -9.94227 | -64.89953 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 88bd1fa5-45ea-3eff-a206-6133c155d335 | -9.9411 | -64.91953 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 0fb222a0-1dc1-3df2-9e5f-7cd7a8d7e93c | -9.94106 | -64.90561 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| aa4370a1-4828-35f5-ba5b-3831db279d92 | -9.93986 | -64.91169 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 88fde3de-1401-302d-9a7c-2bacb13edb90 | -9.93864 | -64.9178 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a84545a3-7d60-3474-8377-3452c7a2abcd | -9.93814 | -64.89993 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 99bbe3dc-3538-3511-9e67-1dd40a327e35 | -9.9374 | -64.92404 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 279e66c9-245b-3af9-bdd0-6aaee6eab052 | -9.9369 | -64.90599 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7a0bd98e-be3a-337b-8b20-857f03bbb26e | -9.93565 | -64.91206 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b0f98089-8d2b-3222-a318-5b1890b4e376 | -9.93441 | -64.91811 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d366ec22-71cc-3a36-9a50-b5e96185ee8e | -9.89102 | -64.67203 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20c4f2aa-0bca-3c79-a49c-7757fce5ee55 | -9.87966 | -64.694 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a151677-c2f5-3f47-8bea-1db51931d212 | -9.37973 | -65.46313 | 2024-10-02 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60a61a7b-cdbf-38e6-a3ab-5c03ea72335b | -11.68314 | -65.001 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e866c69e-ef86-3b8c-8dd6-100d21dee4ab | -11.682 | -65.00668 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8cc2d01d-d446-3cef-b144-97a13d69524e | -11.6814 | -65.00239 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d08ec229-a772-31c1-a9d1-a252a478fd89 | -11.68021 | -65.00807 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e8f3b8e9-b374-3ca0-8d63-e7d2560a9dc7 | -11.67549 | -65.00515 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d14f1f72-999c-3560-8313-227cccc77102 | -11.67433 | -65.01092 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| df5b9104-7e14-37c3-88b3-8bd2fdf7344f | -11.67369 | -65.00658 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81b498c7-5fb3-3f98-9046-222536812f6e | -11.67249 | -65.01237 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41928a46-3d2a-3b08-b499-264803e2714c | -11.6678 | -65.00945 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fb888d34-697a-3617-88a5-6596e374f57a | -11.66596 | -65.01092 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d6feb88-9789-3dfb-97cf-a89f7148a13e | -11.66589 | -64.98513 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96fa0c2d-0aaa-3b5a-be6a-c0fd0437ff2e | -11.66419 | -64.98673 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef46332f-29b8-3bc4-a65b-e568cc97e520 | -11.66009 | -65.01381 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6451d7a8-bda2-37a0-8182-2abb62139717 | -11.65935 | -64.9838 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96db988b-c8fa-3aaf-aa4b-95fafcdd81ec | -11.65886 | -64.97963 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35335b4e-f2e3-3b7e-92a9-c099a582154b | -11.65821 | -65.0153 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8c99b6cf-e42a-3640-830f-0ca3b5227403 | -11.65765 | -64.98537 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdbb168d-4eac-36cf-a029-201728436abf | -11.65113 | -64.98394 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7843024a-58d3-3a2b-8b8e-0b20261f99fc | -11.28849 | -65.27029 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1613ba3-946f-3b6c-bb28-5ca0eb47b65f | -11.28718 | -65.2765 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 850d95a9-899d-36fd-80a9-7a5ae524da75 | -11.28558 | -65.26936 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49c48769-5e96-3d23-a4fa-fca8dccd04cf | -11.28431 | -65.27563 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3749ed1-da40-3679-b4dd-6583e3cd1811 | -16.83284 | -55.91783 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5e0473e1-84d0-328e-953a-1e4dedba71a4 | -16.83139 | -55.90519 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 54ea0d18-2a4b-301a-bfcd-02953ded1300 | -16.83128 | -55.88459 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1c254b58-8049-3015-812e-ac03fa451207 | -16.83071 | -55.90919 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9d94da1a-fb20-330b-a963-f89af361474e | -16.82724 | -55.90856 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c8fed47b-ef02-3660-8f0a-f56be85cc490 | -16.82569 | -55.87535 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0141fa43-fd8d-3d19-a9a0-9f0a73a8fddd | -16.82521 | -55.92057 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e7fe9392-ef7a-3cf9-8abd-c095663f8756 | -16.82501 | -55.87933 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3f5b3cf9-b3ce-30ef-b2ba-c8cf9bc4d727 | -16.82434 | -55.88332 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fea0ff4e-41d0-3546-af61-5935996e9649 | -16.82309 | -55.91194 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 08c985b1-1670-3e06-ae87-70a8b7b2f594 | -16.82174 | -55.91994 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b2c3eb94-d297-3182-bd00-26d092576f3e | -16.82087 | -55.88269 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 38358eb3-8dbd-3b1f-8875-99a7641425fb | -16.81673 | -55.88605 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| eb9effed-cec9-3248-aa03-a78102215ef2 | -16.81546 | -55.91469 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| ea1c4ddb-1128-3f04-a6c0-d2e6bc440147 | -16.81479 | -55.91869 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 256b67ed-339b-34a4-8857-b6aebff759a6 | -16.81181 | -55.87283 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 21e704bf-ea23-3c3d-ad13-c6ea6868113e | -16.80979 | -55.8848 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1b422750-c088-366f-9251-14b6f33c24da | -16.80104 | -55.78899 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c0720098-821d-3ea8-b4d8-901f358aa3ce | -16.78578 | -55.774 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b2b81f59-9d17-3bfd-96a7-9ff8c7eba476 | -16.78443 | -55.78192 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1a469ae6-6bac-3e12-956e-aa8a0a9a6e7c | -16.77171 | -55.91915 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b4db0bdb-e45e-3342-9078-705f0a3a98d5 | -16.77027 | -55.76803 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f7a37af2-6748-3bd3-bf0a-ae7941b01a03 | -16.72018 | -55.4966 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a70fb6be-a1e3-3c29-b420-afccb4b716a6 | -16.71701 | -55.4966 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 07a99c4b-68f5-3314-bedd-80bbeb104787 | -16.71636 | -55.50049 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f9aeaec5-9c66-3437-b905-5763d84dd51e | -16.71611 | -55.49985 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9c572791-0a84-3310-b39b-4305a7b3befc | -16.71165 | -55.50763 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f8a010d4-5739-323e-85c1-28cbb056e56b | -16.70759 | -55.51088 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ecb06df0-38e4-3391-acd9-805a9c6b77eb | -16.70694 | -55.51479 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a54ca49d-d9dc-3a06-a177-d0afcff0b0ab | -16.70325 | -55.55841 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README106.md)
