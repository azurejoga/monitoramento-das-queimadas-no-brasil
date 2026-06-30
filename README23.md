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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99c07d0f-51aa-34f2-b400-6f94bfdfd8e2 | -8.9989 | -45.7191 | 2026-06-30 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f4f5914c-5429-318c-88a7-d8aa3c59bf54 | -13.2452 | -56.7965 | 2026-06-30 15:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 80ae93e9-75b4-309b-9016-99643e2cac50 | -11.891 | -57.3751 | 2026-06-30 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| cdb892b0-c412-3a48-a496-2988ce022a09 | -8.1113 | -50.9417 | 2026-06-30 15:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 70388644-884a-366f-8c27-aa6a85d854a0 | -17.712 | -46.7798 | 2026-06-30 15:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 215.6 |
| 692b3e2c-676c-32b3-a663-f6eb6746af0e | -11.91 | -57.3735 | 2026-06-30 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| bdb9975e-1803-339c-98be-acc10100a169 | -7.7347 | -45.9145 | 2026-06-30 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 91326daa-8268-3c88-bf7d-1d76bcc087ec | -13.2643 | -56.7947 | 2026-06-30 15:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 667.3 |
| 1283b0af-d570-313a-bf83-ed7778f20a0f | -9.0228 | -59.5485 | 2026-06-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 57d2cdb5-3864-3da8-9813-923f174c2e2a | -11.9097 | -57.3935 | 2026-06-30 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| b48aa44e-cc9d-3aab-a6f8-02b486b211b4 | -8.0928 | -50.9221 | 2026-06-30 15:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 230d09ff-db85-3097-bed1-96dde3352031 | -9.0229 | -59.5291 | 2026-06-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 230.7 |
| a261f84f-f993-39dc-813d-c0129cdacff2 | -9.1833 | -58.0584 | 2026-06-30 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 91c6641d-31ca-32d9-8987-386cbf0c4ef3 | -10.3443 | -46.9142 | 2026-06-30 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.1 |
| bca7ecc1-cb30-3d6a-904b-74c015c9251d | -13.264 | -56.8149 | 2026-06-30 15:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 284.4 |
| b570f3b1-7159-32e5-b554-b703c42934f2 | -9.079 | -59.4874 | 2026-06-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 221.1 |
| d0e2cad5-8849-3bd7-8096-749bb072e341 | -11.91 | -57.3735 | 2026-06-30 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 99ed1168-0ba2-381f-a737-4132c21fc4f2 | -13.2643 | -56.7947 | 2026-06-30 15:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 388.9 |
| 62635c87-b7b2-3bdc-89bc-a9fc8ef41e63 | -7.7158 | -45.9163 | 2026-06-30 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 89b54102-c9a6-3753-8632-32ac06f160b0 | -13.2452 | -56.7965 | 2026-06-30 15:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 513576bc-2ea9-34ae-8cb7-26962bfffaf4 | -11.891 | -57.3751 | 2026-06-30 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 962e0568-04fd-399a-9d37-0e3598dc3ece | -9.1647 | -58.0595 | 2026-06-30 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ca21aeae-4856-3023-a67b-e0a686a0dd9b | -11.9097 | -57.3935 | 2026-06-30 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 7b7fa494-7420-3551-910c-779c0cb9e09b | -11.6286 | -59.0169 | 2026-06-30 15:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 120ea126-8da6-3931-b086-e9b29f6f3b73 | -17.7114 | -46.8031 | 2026-06-30 15:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 4307d858-6ecc-300c-a150-947b17f44450 | -9.0229 | -59.5291 | 2026-06-30 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 217.7 |
| 4c7cd44b-ddc0-3bc4-b039-9f4f1b80e262 | -9.079 | -59.4874 | 2026-06-30 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 3be5d3d7-0eb5-314a-8767-a0f15eb5a302 | -10.7162 | -56.2294 | 2026-06-30 15:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 698f3f1f-9bb4-3cc6-86a6-553c670aad30 | -8.1113 | -50.9417 | 2026-06-30 15:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c6a9488d-9922-3533-b003-92c8790d5aaf | -8.0928 | -50.9221 | 2026-06-30 15:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 179.7 |
| a2923a21-ea52-39ed-96ba-03aaa278be02 | -9.1833 | -58.0584 | 2026-06-30 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 740b69f1-12fd-3236-bc8e-53b379f73f26 | -17.712 | -46.7798 | 2026-06-30 15:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 46a06444-c31f-39f1-b13e-ea56d6da25e5 | -9.0228 | -59.5485 | 2026-06-30 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 229.9 |
| af28f682-0ca8-3ba6-a69b-c20dd90f70ea | -13.264 | -56.8149 | 2026-06-30 15:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 249.8 |


