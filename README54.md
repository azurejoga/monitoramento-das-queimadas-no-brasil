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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72fc5b82-d8c4-3e5b-bee0-b4b4cbba7c46 | -19.2386 | -46.86935 | 2024-10-02 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 03a1e607-fbd0-3f18-846c-b2a271e6836c | -19.23796 | -46.87146 | 2024-10-02 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06e6b6e4-8a29-3993-a5bd-8e87176a6e25 | -19.23363 | -46.863 | 2024-10-02 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fd5d728a-25bb-3352-a9ed-9c4bb9fc7ad0 | -19.23252 | -46.86798 | 2024-10-02 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1f2dea01-9c14-3895-9a00-29c98745a748 | -18.9822 | -47.29514 | 2024-10-02 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de407933-11ef-3c93-befe-afa3286665bb | -18.98108 | -47.30002 | 2024-10-02 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d3f5986-b571-319b-9672-ce01904c1d40 | -18.96373 | -41.52458 | 2024-10-02 03:32:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8bccaf7-f485-3a3a-9b2c-5f2df5f7550e | -18.93005 | -42.83958 | 2024-10-02 03:32:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 68288a3e-e646-3e70-8d01-e756ae80a601 | -18.92861 | -42.84016 | 2024-10-02 03:32:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4a8aa779-28ce-357d-adac-0a5c56782412 | -18.78765 | -41.90421 | 2024-10-02 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5ec8f6cc-cac7-39d3-814e-b557cb10feb3 | -18.78662 | -41.90548 | 2024-10-02 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a8021de2-1722-378a-9ced-02ec7807926d | -18.78313 | -41.90331 | 2024-10-02 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4e60161e-0bd1-3d43-ab60-703b78d91626 | -18.78302 | -41.89978 | 2024-10-02 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8d0e4d90-61fb-3f20-9e9e-f637a1a531dd | -18.7821 | -41.90456 | 2024-10-02 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9887b62a-87c3-3d0a-bd91-7091c73e6835 | -18.52305 | -42.23533 | 2024-10-02 03:32:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0b42753f-18a6-35d9-8605-5bc0ebcc1900 | -18.52029 | -42.22504 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 97ea4586-09b0-3e66-b00b-93761e0aeb24 | -15.1628 | -46.24298 | 2024-10-02 03:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67bdcebb-64a6-3206-8fef-b5e98b28fe1e | -18.5194 | -42.22948 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 53709c31-5f16-3038-a0c2-d796bcab5612 | -18.51806 | -42.22276 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 52e577e8-0e92-3f47-bcca-a03beeb367cc | -18.51748 | -42.23902 | 2024-10-02 03:32:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6653796f-f871-3378-aa81-a4dcc96aa0e1 | -18.51722 | -42.22711 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4a2cdcec-7b56-3f04-b35d-ed570799d931 | -18.51569 | -42.22393 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3d278528-d5da-3fd9-bb83-e87d12db3d57 | -18.51482 | -42.22822 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 099e8777-287c-3111-8b75-90be80035cac | -18.51262 | -42.22596 | 2024-10-02 03:32:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7c32cdbb-192f-3c8b-bdf9-daab745ca9ab | -18.38517 | -44.01484 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9805a978-397d-358d-af62-6c47cf3a9873 | -18.38432 | -44.0189 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d34b2f07-6e23-30ae-8242-cac5421024fd | -18.38299 | -44.02522 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbf0c74e-281e-389b-8750-7a361f90fe7d | -18.35539 | -44.02699 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e9121a-e43b-3d33-b933-33d984c03fb4 | -18.35522 | -44.02851 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a1a4629-d0fd-383d-b6e8-f3735eafbe3c | -18.35461 | -44.03067 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0086e6f7-1881-3780-b481-60ae07b29383 | -18.3545 | -44.03208 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac4cbabe-462d-35fd-81bf-9cbe5be92854 | -18.3511 | -44.02154 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aa2f530-4a3b-3e68-91c0-edf3c87cadb3 | -18.35088 | -44.02312 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cd45330-ddd9-3e5d-91fd-572b6059c87f | -18.35027 | -44.02549 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51a57a20-0c50-3ad4-a3bb-ce106e7fe06c | -18.35008 | -44.02705 | 2024-10-02 03:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85d86a6b-74da-3f3d-91c4-61afb89c2928 | -18.34324 | -43.0464 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a5815ffc-f07a-3b0c-b851-1889d58fcba1 | -18.34198 | -43.05251 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d72099cb-84be-3919-9a0a-f23b0872f1e9 | -18.3409 | -43.05079 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 99a8c7dd-3ada-3d7b-abc6-4dea28dc07ad | -18.33837 | -43.04524 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0030597c-2d70-3392-96e8-b41071f6ff3a | -18.33719 | -43.04376 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 135e3777-6a82-3e9d-87a5-223eccc0cdcc | -18.33718 | -43.05103 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1ecb0214-736f-3573-8f3a-81dfd64a9e9c | -18.33607 | -43.04938 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3adb13a9-20e2-3d8f-bb04-95341b29dd6f | -18.33168 | -43.25259 | 2024-10-02 03:32:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fdb77b4-ac96-3d0a-a7e7-37c4df2a4a22 | -18.32996 | -43.23579 | 2024-10-02 03:32:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| acea4f1d-1be7-3678-b681-02699fbd6069 | -18.32896 | -43.24064 | 2024-10-02 03:32:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0401d8b7-b898-305b-85d3-e7e8cfd06bce | -18.3268 | -43.25117 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b4dff7b6-084a-36f0-979f-92015d8bf94d | -18.32511 | -43.23424 | 2024-10-02 03:32:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f90ec342-8cf2-35f7-8a66-48d41a79944d | -18.3241 | -43.23911 | 2024-10-02 03:32:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7525ae4b-bdd4-3157-8984-681d9f0a1caf | -18.32303 | -43.24433 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c0842d23-e34e-373c-8518-bf82c40400e3 | -18.32183 | -43.25013 | 2024-10-02 03:32:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2bc2b22e-8d56-3b20-93cf-dde5a173b70a | -18.20341 | -43.95035 | 2024-10-02 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a3ced94-fccc-34b5-9726-14f5b46b7b1a | -18.20276 | -43.95345 | 2024-10-02 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c81111a-58ee-39d7-9f86-720ada816e0d | -18.08282 | -46.14368 | 2024-10-02 03:32:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04eef817-0b45-3448-b640-eabba2e6fd2f | -18.07146 | -42.61915 | 2024-10-02 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 443130d3-affc-3ad8-bcc6-17e666db93c0 | -18.06875 | -42.60764 | 2024-10-02 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 78a8b326-431a-34c4-a4dc-773a0ca8df70 | -18.06775 | -42.61267 | 2024-10-02 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3bedff55-15ea-3322-84ae-7c6b80413d04 | -18.0667 | -42.61799 | 2024-10-02 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 50b7a1b0-919a-33dd-b855-5b2fc10a53df | -18.06293 | -42.61185 | 2024-10-02 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8408174f-9c9a-352b-8ea1-f9f9d17e1ac9 | -18.06192 | -42.61693 | 2024-10-02 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 10ff431c-ca33-3c0b-abd2-b6e822aa6b12 | -18.05121 | -48.60177 | 2024-10-02 03:32:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8830f966-ba5f-3094-b211-dd5f87db8137 | -18.04455 | -48.5994 | 2024-10-02 03:32:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f55e2f3c-e7d2-36da-b7d5-3534873fce73 | -17.92286 | -44.3362 | 2024-10-02 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 073c343b-968a-3141-995d-fc90f6ea4825 | -17.91757 | -44.33472 | 2024-10-02 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbda303e-aba0-374d-ac27-2e1deb87043e | -17.87496 | -42.19396 | 2024-10-02 03:32:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7db36f19-6114-34b3-9c3a-ecbf16e1482a | -17.84263 | -41.42464 | 2024-10-02 03:32:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4c47ea5e-b185-3708-9a2a-8ea2f2447c5d | -17.71001 | -42.37526 | 2024-10-02 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0489bb68-d532-350c-b61e-0a4b37e2c1e9 | -17.70999 | -42.37808 | 2024-10-02 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 727a6b6e-e235-3765-906b-1b9256a801ac | -17.70527 | -42.37426 | 2024-10-02 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed19def2-c624-30d2-80f5-bba50f0f1b55 | -17.70525 | -42.37709 | 2024-10-02 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b551bf3-ca78-3b62-9763-cdab46da45c8 | -17.63462 | -43.25492 | 2024-10-02 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ff4783d-6255-3c22-9545-4bd16c0c9c40 | -17.62963 | -43.25368 | 2024-10-02 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6be06477-e4d5-330d-99c2-9c788bd35851 | -17.55511 | -44.99944 | 2024-10-02 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad761f4f-3b6d-3504-a5ae-3e29247bf091 | -17.55428 | -45.00332 | 2024-10-02 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 442136c1-0662-3a56-8c89-b8ded46046c9 | -17.20466 | -39.51396 | 2024-10-02 03:32:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5042d9dc-a2bc-3df9-a47b-36f53e1dd144 | -16.69215 | -47.82991 | 2024-10-02 03:32:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42513320-7cea-3e0c-91a8-7e0f57342f81 | -16.67879 | -43.88244 | 2024-10-02 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19007a00-4fb4-3000-9acb-2d275e957b7d | -16.4303 | -47.00389 | 2024-10-02 03:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50a88896-74f7-391d-b1fa-9b27a90c9c53 | -16.42957 | -47.0051 | 2024-10-02 03:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c88f6047-a41f-3925-8523-4abfc5d79ac0 | -16.4291 | -47.00937 | 2024-10-02 03:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8c57180-d5d8-3b39-bc97-058a5bd51a36 | -16.42835 | -47.01051 | 2024-10-02 03:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da2d8bdc-1fb7-3755-b418-7529ea8a1c42 | -16.42255 | -47.00836 | 2024-10-02 03:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f247cc5-9481-382b-a70c-027df37c8d8d | -16.41802 | -44.09458 | 2024-10-02 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 620dd2af-77f7-3350-ab91-02635e524d0a | -16.41341 | -44.08951 | 2024-10-02 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a86823f7-9c3b-3773-9dbe-5fa27b537a94 | -16.37888 | -40.5435 | 2024-10-02 03:32:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3deeb7f-fee1-35c0-b2b4-a9c745c85f8e | -16.37455 | -40.54265 | 2024-10-02 03:32:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b6492802-8c27-3bd7-ad0f-ed076c781e98 | -15.7622 | -47.66876 | 2024-10-02 03:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2351a6f7-969c-3fdd-985a-a0fcc6eb8eb3 | -15.76163 | -47.66907 | 2024-10-02 03:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd640bd7-1728-397c-8b13-57ed83f2f5cd | -15.76061 | -47.67581 | 2024-10-02 03:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94db9240-f693-339c-8a82-55e2b6709a6f | -15.76008 | -47.67616 | 2024-10-02 03:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93f27cfe-1c64-3424-981e-6714b6894602 | -15.45046 | -43.62253 | 2024-10-02 03:32:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 835cd94f-4210-3683-a599-eed202b71760 | -15.44513 | -43.62129 | 2024-10-02 03:32:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4f626f7d-a794-30ef-8062-5bf9dea19e89 | -15.36507 | -47.42806 | 2024-10-02 03:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdc3ed12-4a90-374e-8597-735b6ad374f5 | -15.36364 | -47.43441 | 2024-10-02 03:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f3e5a30-6a2d-3f64-ad22-fc2b2e3cdd5a | -15.34539 | -46.73509 | 2024-10-02 03:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6654f995-f53b-34b8-8af1-3af8597e727f | -15.34416 | -46.74073 | 2024-10-02 03:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56545a74-05b9-354d-aa78-05219f4bc0f0 | -15.3389 | -46.73373 | 2024-10-02 03:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f004ffd-5588-3cb0-8219-427c6a6704da | -15.33369 | -46.72654 | 2024-10-02 03:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe5ecce-faa7-3cc5-9166-5f4ac9340de5 | -15.33242 | -46.73235 | 2024-10-02 03:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 091c5cfa-3919-3f1e-929d-e8ccdb44aaf4 | -15.20741 | -47.94221 | 2024-10-02 03:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9a38c67-b7df-3dd6-8c28-c4e1940372ab | -15.19907 | -47.9469 | 2024-10-02 03:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
