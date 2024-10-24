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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc1ed245-d59d-37b1-800a-dbd14c1a7624 | -7.98705 | -50.69417 | 2024-10-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd8500f9-9391-308a-a41f-c5e58f4381c8 | -9.86032 | -51.18622 | 2024-10-24 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14e2b44e-87de-3e88-a74c-cba0ec616553 | -9.37773 | -51.88244 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b56ef4d0-18b6-3109-9875-3431586b3a4c | -9.37703 | -51.8866 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8134443-7945-3a58-a219-2769b51c18d4 | -9.37409 | -51.88187 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3323700-1933-3e87-8f23-2b2b75ed6b6d | -9.37339 | -51.88606 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a983c98-9bde-3a83-bad2-65803b538163 | -9.37269 | -51.89022 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69b7c327-e05f-343c-a3de-5431738f1f84 | -9.37045 | -51.88129 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d04144df-cce9-306e-b7f8-2630f2190292 | -9.36975 | -51.88548 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edea40d0-64f0-3318-853e-17fd8020550e | -10.15946 | -51.55421 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc5a3ac9-ac00-3fb5-8a66-44c292263daf | -10.09844 | -51.12837 | 2024-10-24 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c8ae67b-6762-30c9-a8fe-2837c74e5a95 | -10.09496 | -51.1278 | 2024-10-24 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33d5d4fc-effc-3896-886a-5faf56f7a04d | -10.74318 | -52.14195 | 2024-10-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd02e8e2-6fdd-3ac0-bed4-571edd1b90d2 | -10.67027 | -51.82024 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c81ca7a-194e-372f-91bb-7465d5897a1d | -10.66749 | -51.82101 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9819620-e9a1-3d27-9c7b-1a9c922fb746 | -10.60525 | -51.90843 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4993108e-75b5-33f1-9287-4db40e14d8e2 | -10.58299 | -51.47355 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a666605-ca02-31ec-b0fe-4e485528b914 | -10.57978 | -50.91389 | 2024-10-24 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbc144ab-7a22-3cd1-a87a-354a648c0764 | -10.51683 | -51.85197 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e91417e1-f812-3f3a-91eb-730c79975fb5 | -10.51395 | -51.84715 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50ac596d-5fab-37e5-b4aa-870e7ced3b36 | -10.51326 | -51.85135 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfaa22e5-75c2-341c-9670-132b1e58f861 | -10.47728 | -51.9565 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd15fb1-5e72-397b-8fb4-5aca6b3bfb02 | -10.47368 | -51.95591 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44551902-9792-35da-93f3-8e9d09a65f2b | -10.36748 | -51.39356 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db22b834-131e-3a0d-a618-cad19de4cc40 | -10.34035 | -52.01233 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0cdb023e-0991-32c1-b83e-a37ee88d79bc | -10.33673 | -52.01171 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0613c3-8bb1-3647-b0c3-cd95f3315851 | -10.30802 | -51.88669 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 517cd408-18fd-39ff-a7af-5f049c42745c | -10.30733 | -51.89084 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 744ba299-3291-34fe-841b-88149cc87675 | -10.30304 | -51.89442 | 2024-10-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59f04687-2a9e-3ea1-9920-f7e933988acf | -12.34245 | -51.20415 | 2024-10-24 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e945ec3a-ed84-3c44-a466-3128470b5087 | -12.29416 | -51.17648 | 2024-10-24 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 300ab57a-e5ec-3e1d-b3fb-154895623ef2 | -11.44506 | -51.48781 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4543e312-57bb-3389-bfe8-5817045680e4 | -11.44157 | -51.48723 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56447f00-31fc-3b6e-9011-64eb8a8cde8d | -11.11853 | -51.92189 | 2024-10-24 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5118ad00-7d5d-3847-8d74-acf550891542 | -11.10002 | -51.55352 | 2024-10-24 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b0a8f3b-c72d-3e6d-8322-0af9b1cc14be | -11.09651 | -51.55294 | 2024-10-24 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fe55909-e44f-35fb-a1a9-9865507daf77 | -10.99109 | -51.96544 | 2024-10-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3194ed80-076d-3ab8-b19b-5cb446116fda | -12.4693 | -51.3307 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3f22152-a167-341c-bc5e-18cd0123fa73 | -12.46868 | -51.33452 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d28b093d-7400-33a9-8053-c655955b6df8 | -12.46587 | -51.33012 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d8620c1-ddfb-36f2-af70-b0b179f8494e | -12.46525 | -51.33393 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfe99c90-b4e8-3774-a723-16c4e01a647f | -12.46244 | -51.32954 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cbc3a47-86c3-3a76-a2f5-3d35cbcef129 | -12.46181 | -51.33335 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51d6041b-2403-37b7-8072-8d4d78f90c4f | -12.42808 | -51.09032 | 2024-10-24 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3afb38a7-d9a0-30c1-8e50-4bae8f53ce92 | -6.40633 | -51.71106 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8791b10b-05cb-357a-9663-e51b9ad19782 | -6.08902 | -51.21643 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6655bc19-782c-3db0-894e-6bbef2ba0b02 | -5.62457 | -51.38975 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82cc6daf-0702-381d-8d22-5a07bc086d3a | -5.62382 | -51.39424 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f060b837-a81d-3e9e-ab9e-f20f4c658d15 | -5.62312 | -51.42143 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8ed46f1-caa7-3be8-b6a3-598fa25ef49e | -10.27178 | -52.17368 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3605ebd9-9c59-3a4e-a4a0-7455d232e598 | -10.26813 | -52.17307 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89c51072-89d1-348e-8c37-40c79379e12e | -10.26742 | -52.17739 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4941561a-6753-35a2-a3b2-4f28736452b7 | -10.26377 | -52.17679 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8324ea4-0c06-349f-9bbb-e53ea41b6068 | -10.28051 | -53.80018 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc6f78e1-83a0-3191-a43c-14468867368c | -10.20116 | -53.87078 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb962811-9d82-310a-bbef-52543b95d70e | -10.20054 | -53.87441 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a42a6fb7-d19b-372a-883d-e22b4cb3a34e | -10.19993 | -53.87804 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5672f886-3af0-38d9-ac82-261ad0f71aa1 | -10.19713 | -53.87004 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e36cb9f-1b59-364b-9403-025651d7e1af | -10.19651 | -53.87368 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9ba12ba-1b22-3ce5-9af3-4b73bb98f228 | -10.19589 | -53.87734 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59525d35-0a3e-32e6-b239-530493fde884 | -10.19309 | -53.86935 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3dc9ccc-5e9c-318e-92fe-7ba8ba3ab973 | -10.19247 | -53.87299 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7d71aea-af73-3c23-b039-e6895ea44ce8 | -10.19185 | -53.87664 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d661b180-5350-3ef7-b8e8-edf25809ccda | -10.50178 | -54.55495 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e09056af-073b-3c71-98b1-3a47be3e1b60 | -10.49689 | -54.55817 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a4f27f2-ea3e-33f3-bf2d-29dc9a3a1839 | -10.47436 | -54.44053 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a63f9c30-8f8c-35b6-9fa8-d46c5ab22179 | -10.47292 | -54.42435 | 2024-10-24 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc4fdf94-e5bc-3b79-a9a1-4508969cf777 | -11.52167 | -54.32074 | 2024-10-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af0d5cd-d4e3-3e96-b6ef-a2eb5ca80769 | -11.4238 | -54.30606 | 2024-10-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37ae468f-f85b-3980-be30-fbc389ca4fbc | -11.41973 | -54.30536 | 2024-10-24 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f544af-9e90-35eb-bc80-444147a25bac | -11.31454 | -54.33227 | 2024-10-24 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76b700c-cc8a-32b8-8fc0-371c424eb292 | -4.42413 | -55.43332 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c9d09e8-6d88-32e2-8064-e0242c457b15 | -4.3965 | -55.04767 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462c706b-e077-3d42-b024-5d3a37aad603 | -4.38762 | -55.18853 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57d7a285-e44e-3a66-b0a0-a0d792777763 | -4.14746 | -55.15111 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b255b915-1b17-3f92-ac7a-cc8f24e11771 | -4.14651 | -55.15667 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7455b4eb-e86b-3777-bfd8-8adc02ccdb44 | -4.14254 | -55.1506 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c4abe1e-9cff-3701-816a-0621a5cbe2a0 | -8.30993 | -55.10312 | 2024-10-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f449cd51-da1f-3d39-8339-db7e136c47e6 | -8.30913 | -55.10771 | 2024-10-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 86ead72d-691e-3b8d-9ccc-2fa8f70e697c | -4.53999 | -55.75054 | 2024-10-24 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8269564b-afd3-3069-8233-ee9c9eb786f2 | -4.53947 | -55.75362 | 2024-10-24 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d56101f-c744-3ef2-a4b1-0cbd22e0e0fc | -4.53444 | -55.75275 | 2024-10-24 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99ab0fac-aebc-3235-af2d-3fb63cd37a97 | -4.20238 | -55.55451 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 694e69b1-0ec6-3ab2-bf35-bba8fe63c8ac | -4.2019 | -55.55731 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 402c25f2-39e2-3bfd-a6c1-e8f56635fa95 | -4.19692 | -55.5564 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8d008d8-79de-353b-b6d7-f3564143aa21 | -4.19534 | -55.68755 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4bd494-366e-398d-b0a2-aa4e47a6a1ee | -4.19484 | -55.69049 | 2024-10-24 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b662bec4-d5a0-346a-9b8c-9eb0fc197101 | -6.75865 | -59.11818 | 2024-10-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 33957759-7824-3012-b0c4-ca448a22e518 | -1.5878 | -53.3089 | 2024-10-24 04:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e523e79c-16de-3d9b-a6fa-fde411a65425 | -2.9578 | -50.4198 | 2024-10-24 04:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 503b5c54-7539-33e4-9e35-e05354cffa63 | -2.9763 | -50.4193 | 2024-10-24 04:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 29e80b5f-b614-335e-afca-5fca6a35e451 | -3.1607 | -50.4556 | 2024-10-24 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a7ff0d7d-05be-3381-ae2d-870ed284e3a3 | -3.9396 | -46.4229 | 2024-10-24 04:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 2a2aab0b-1b34-3648-bc5b-cfe577386c01 | -16.63528 | -40.84846 | 2024-10-24 04:36:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94d22465-c6a1-3dfc-8116-e4e7a32b8107 | -16.63491 | -40.8517 | 2024-10-24 04:36:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9bf37e49-ef42-38f7-9517-9aec19e011b9 | -16.54501 | -41.6326 | 2024-10-24 04:36:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2ab57890-1eca-35eb-a77c-f83f2e1c7989 | -16.3405 | -42.20509 | 2024-10-24 04:36:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| db4e2052-50c0-37c1-ab0f-f1448636eca1 | -18.18503 | -42.86836 | 2024-10-24 04:36:00 | NOAA-21 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f28fb25-5235-3f77-acaa-2f4c1795e94b | -14.94835 | -43.16882 | 2024-10-24 04:36:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d35fd9d3-5cdb-3140-83fe-123bc0b11280 | -14.28834 | -43.03709 | 2024-10-24 04:36:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
