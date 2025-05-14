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
| cc2c3898-2741-3fd0-b46e-a493a6ce2863 | -12.86769 | -55.05496 | 2025-05-14 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1569331-49f5-34b6-be43-8503bcabcd50 | -10.52307 | -59.38419 | 2025-05-14 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550363ae-b700-35a1-876a-0e4487ebcbed | -13.98103 | -56.79813 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 119ee8ce-6bc0-3e6d-ab83-e5d1994f8c37 | -13.96177 | -56.78585 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edbacce3-3cbe-32c2-93b4-9ad33cc7dc1e | -13.05149 | -53.72291 | 2025-05-14 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3926da9d-ee55-39d4-a55e-c0814e23ce54 | -12.68816 | -58.13022 | 2025-05-14 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 763f9b78-0ed6-3b0a-8225-637faf2ad125 | -13.95632 | -56.78813 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4d5ea57-4b96-3759-8be6-a0c5ef6d629e | -12.50189 | -57.21682 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9acac9a-a6ac-3638-9a76-3a9d83d6c39b | -11.65824 | -54.95676 | 2025-05-14 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b70c4e-a4ad-3d4e-88d3-8f0fa4bd4898 | -13.06688 | -52.02139 | 2025-05-14 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5eb03bd5-828a-39c6-9ea5-5b35c02fb099 | -12.86673 | -55.06279 | 2025-05-14 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 514e221a-1bb1-3f76-9f41-fa2c62c79c39 | -13.96612 | -56.79291 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0a3c342-c7b0-356b-bf73-7715a4de4c17 | -12.86966 | -55.06406 | 2025-05-14 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5700244f-0b64-3750-9e66-00b6485a42eb | -13.09263 | -52.28562 | 2025-05-14 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f27215c5-d381-3eec-b09a-42f984c054f3 | -13.97592 | -56.79753 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5457f638-aadc-3577-87bc-617ed3657bad | -13.62056 | -54.88097 | 2025-05-14 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd22f301-4034-3a16-8784-ce49893a88f8 | -12.72563 | -54.96962 | 2025-05-14 05:36:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75d25e1f-a590-37f0-80fa-dd40b14cfe60 | -12.50571 | -57.21388 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7d57393-21fe-3e72-af29-ef3a992c05de | -13.55861 | -52.87893 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2f26d22-1107-361d-b551-40206900e2e4 | -13.96575 | -56.796 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63610546-2f82-3c9f-a42e-76f43817f1d9 | -12.50018 | -57.21866 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc1770b6-6c43-3431-939c-28084f33760c | -13.95559 | -56.79432 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b7bbafd-0710-35ee-b07e-45fdc034d951 | -13.05195 | -53.72352 | 2025-05-14 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5450a2bb-a858-326d-b7ff-6612a7910e4e | -12.86721 | -55.05888 | 2025-05-14 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33f563a1-a7b2-3e5c-82da-d916e1d25a5b | -11.6587 | -54.95302 | 2025-05-14 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58528c6e-9e21-332d-912b-1697ecfc4991 | -12.50503 | -57.21937 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5303b81-6314-3988-bc4a-edff7b6bb76e | -12.50674 | -57.21751 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c096d0fd-ffe4-39bc-aa96-c1044eda2564 | -10.00309 | -62.58163 | 2025-05-14 05:36:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec336d5f-b6f0-3cd3-8cc8-d5183aa9126b | -13.96215 | -56.78273 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30247f2d-bdae-39b9-9eeb-d9a9926be4d4 | -12.51057 | -57.21456 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb2e3dee-71bf-33df-80b8-5083b5e850b1 | -10.04078 | -64.97482 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ecd1948-da93-380f-b23c-345df6a94994 | -13.56644 | -52.8728 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44944542-554c-37af-8bdc-4277fa810dd1 | -13.95595 | -56.79122 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7565b450-da07-3344-a6bc-e711baec37e9 | -11.91434 | -54.40291 | 2025-05-14 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd6f3c42-3ab0-3178-9779-ef8a5b2efa79 | -9.92928 | -65.0144 | 2025-05-14 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 613d64c9-62b0-35e6-9296-c7a1d2e26cd5 | -11.91964 | -54.40795 | 2025-05-14 05:36:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9897037f-be70-3d5a-bf3c-18186fff953d | -12.6836 | -58.12956 | 2025-05-14 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e324407-51d8-3992-b420-86c6f82300c1 | -9.67525 | -65.53613 | 2025-05-14 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54d5f71c-4c38-35e9-a6a3-224d013f5e41 | -12.50086 | -57.21318 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51f3cd4f-8b44-3efb-8976-f0c23596ce69 | -12.72516 | -54.97354 | 2025-05-14 05:36:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54bc067b-b653-3871-ac6c-55ac4dd322bd | -13.56575 | -52.87391 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ced8480-dc90-3ec7-9b4d-d1776cbe5345 | -13.96686 | -56.78666 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a85ad1d5-076f-3b6c-9559-64352077f6f9 | -13.6732 | -53.94676 | 2025-05-14 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c7a6a1e-8c66-330b-b161-444f84e3abd3 | -13.96067 | -56.79515 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0346a9d9-1ad7-32ce-b699-9cb2a5768040 | -12.50117 | -57.22229 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4099ddb4-41a7-3bea-8164-bd14c84cf93e | -13.67933 | -53.94735 | 2025-05-14 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd14ba0f-3339-3a22-bb18-1095141f64b9 | -13.56579 | -52.87854 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 744eea52-fa60-3234-b707-220827e5adde | -13.98031 | -56.80409 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0adb125-cb79-3a85-a7fb-725c21c92567 | -13.05203 | -53.71807 | 2025-05-14 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee9199e-d3e5-344f-b38e-44a257d21687 | -13.98543 | -56.80459 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc8126d1-071a-31d9-b1c8-6f9c2e7f2022 | -9.93204 | -65.01845 | 2025-05-14 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65aa7010-14ac-3052-adb9-caddb6b9db32 | -12.50746 | -57.21204 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df45b244-bec4-38c1-8e4a-390f8bc58a53 | -13.96104 | -56.79206 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 68043aef-4a05-3566-a31e-3d3036a9cd80 | -12.68753 | -58.13499 | 2025-05-14 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ac03b0-4350-3d45-9b32-58834deeb05c | -10.04022 | -64.97832 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cb4d833-c02f-318a-9d6c-acf736e60df5 | -12.49704 | -57.21613 | 2025-05-14 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3036aa8-b1d8-33a3-86d9-2d531c12b415 | -13.96649 | -56.78979 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d67785c7-1957-3292-8e08-01077dea0c6a | -13.96724 | -56.78353 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 988a6a59-55be-32e1-94e0-cbe0bda35525 | -13.05252 | -53.71868 | 2025-05-14 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 815b9b95-8398-31c8-87b4-097a67acd789 | -13.9614 | -56.78896 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e28faa0-4e08-3237-93ed-a6ffda2a9cfb | -21.71799 | -55.37761 | 2025-05-14 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1765bc33-dbb4-3e31-a257-e0e3ebe91507 | -21.71829 | -55.37159 | 2025-05-14 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22b3a807-b46e-3e12-a933-89312d83afc1 | -21.60416 | -56.04259 | 2025-05-14 05:38:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 976ad6aa-df44-3c8b-b42d-b1cb334d5481 | -21.71788 | -55.37659 | 2025-05-14 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c1a0c4a-c8f3-39c0-b8de-2db181a61ea8 | -21.60377 | -56.04697 | 2025-05-14 05:38:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3405fc21-a3e0-3582-a68d-96331169efd7 | -21.71843 | -55.37263 | 2025-05-14 05:38:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3a1e15c-b831-304a-9e26-2ca7de571d3f | -15.2755 | -43.0758 | 2025-05-14 05:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 53.9 |
| 6eea8253-1e77-343c-b564-8c159a46293b | -12.5009 | -57.21302 | 2025-05-14 06:27:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6af94aec-f7d2-3869-9063-8c27d940d43c | -9.25256 | -60.31676 | 2025-05-14 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c98b08a5-a12c-3edc-a78b-bce6ffa2c77e | -9.25999 | -60.31341 | 2025-05-14 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8713cb52-97e7-335e-9327-0ee96cf53c48 | -13.96253 | -56.77766 | 2025-05-14 06:27:00 | AQUA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8943b36d-db86-3e3f-8130-e1248c829da8 | -9.25411 | -60.3067 | 2025-05-14 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f06895e8-e172-3503-9f14-1051d97a62f8 | -13.97844 | -56.80127 | 2025-05-14 06:27:00 | AQUA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cbbf5759-0ed1-3e9a-adb7-dde97a1d457b | -13.96108 | -56.78807 | 2025-05-14 06:27:00 | AQUA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d8540235-71bb-3211-909e-01a1d979ccf2 | -12.7706 | -48.9279 | 2025-05-14 10:50:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| fe3c70ea-e75a-3cf4-94ca-3352f207ff17 | -9.54116 | -37.19016 | 2025-05-14 11:40:00 | TERRA_M-M | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c50644a4-7615-3d0a-ad83-278629d0fc1b | -6.34086 | -37.85122 | 2025-05-14 11:40:00 | TERRA_M-M | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c6a1616c-bb50-3405-864a-699e9a365c78 | -9.3023 | -37.78976 | 2025-05-14 11:40:00 | TERRA_M-M | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1824a3c9-131d-31a1-afd5-b202860b7544 | -7.45219 | -37.14434 | 2025-05-14 11:40:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 04d94c56-fd45-323e-9f5a-dcc9e8d9d3d9 | -9.75641 | -36.98059 | 2025-05-14 11:40:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 17825443-6860-325f-a1b1-c099305c127d | -9.49983 | -37.02725 | 2025-05-14 11:40:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 248b7e08-2320-33c0-a494-ad8db8fc0a75 | -6.61659 | -44.76958 | 2025-05-14 11:40:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6273fa72-1147-3fb9-9ed0-33179f8a9f5c | -6.62008 | -44.77823 | 2025-05-14 11:40:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 39832436-96a8-3979-84ff-6513df212b95 | -7.45068 | -37.15436 | 2025-05-14 11:40:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c3dfe809-027b-3b89-be86-92c07cebe56f | -6.1791 | -48.0712 | 2025-05-14 12:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c775bc55-bfe7-3129-af0b-c4b94aa2cc33 | -9.6825 | -49.6995 | 2025-05-14 12:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f7a2eb88-1472-3e30-806a-fde362bd6ebc | -12.3519 | -49.9617 | 2025-05-14 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2c3f318a-09d8-36f9-9ee8-4d2e169262bf | -10.8379 | -49.4706 | 2025-05-14 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 358.5 |
| cb4db242-441d-34e5-9e07-9ddb463d9f4d | -6.1791 | -48.0712 | 2025-05-14 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 236.6 |
| 4ef0b92e-85f9-3ad6-857b-ddd1a34881f6 | -6.1977 | -48.0699 | 2025-05-14 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 4012e8f5-f260-3be3-9665-5bb420b08ad2 | -12.3519 | -49.9617 | 2025-05-14 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e93227d7-570d-3012-bd49-9fc691d18afd | -10.8379 | -49.4706 | 2025-05-14 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d732ac48-379f-3852-a2fd-adf5ec39ea2e | -11.8984 | -49.6931 | 2025-05-14 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 70d8907a-2bbd-3485-bb17-7f9184447678 | -6.1977 | -48.0699 | 2025-05-14 13:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1dfb1e3a-49b4-3344-9090-f39ec39be041 | -12.3519 | -49.9617 | 2025-05-14 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 70e38a9b-5e06-34b8-aab4-7feaf4361ee6 | -6.6211 | -44.7668 | 2025-05-14 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 19e41ff3-08ad-37af-8013-e50f4d0c1fd3 | -10.8379 | -49.4706 | 2025-05-14 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 384.6 |
| 51758b76-ae9e-3106-9706-3620ed3b9f6c | -6.1977 | -48.0699 | 2025-05-14 14:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 01da3600-23f6-3227-b46c-2380886639b2 | -12.3519 | -49.9617 | 2025-05-14 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| bd0e9581-010f-368a-8089-a96776d357a7 | -6.6211 | -44.7668 | 2025-05-14 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |


[Clique aqui para ver as próximas entradas](README12.md)
