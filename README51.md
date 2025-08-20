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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b21f780e-b549-308d-8e1d-448a5ef0c5e3 | -13.18673 | -54.95634 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0adb478-3d32-3ee5-bb83-969df7c80786 | -19.85788 | -49.82236 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 683b9464-3b39-3258-8b15-7fc1a1cf9a3c | -16.34799 | -50.1792 | 2025-08-20 04:59:00 | NOAA-20 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ce20089-e0e6-3117-b664-4a236991124f | -13.35233 | -54.40572 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 716541ec-434d-3db7-86aa-9ea6ffe387d4 | -13.33097 | -54.40985 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eb6d9c2e-86dd-3aef-b229-f3fd9ae0f4b0 | -14.45941 | -48.37937 | 2025-08-20 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 133e8ff4-71c1-369e-84c9-9b6eec1d74d4 | -14.63179 | -54.88341 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00c5c189-eea0-37b9-aef3-c252af1cebe7 | -12.9749 | -56.8772 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c3901f6-35b3-39d9-87e1-a7b0559bee62 | -19.45543 | -47.1925 | 2025-08-20 04:59:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7959ce9c-cea0-344a-b7ca-79b62ff8d0d3 | -13.3349 | -54.40671 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a87d628c-d8bb-3ed7-b507-3be25d6b5bb5 | -13.15784 | -54.94436 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d39a2833-c641-3ff8-9c80-b002076bc654 | -13.03376 | -56.84651 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 564101a1-9cd9-3c25-9868-12b97c820e06 | -13.18395 | -54.95222 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 441188cd-a394-3c65-b262-5c3b2de36eb6 | -14.54995 | -53.17752 | 2025-08-20 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f57e83ef-c365-3dd8-8b45-13339e540635 | -13.43473 | -57.09894 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3312fb2e-c633-3851-9c01-835117157cde | -15.0006 | -54.82383 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe46f9fb-3b3a-3bf3-a4c6-7e69f0e6188c | -13.02375 | -56.8448 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d7957ad-44d8-343a-948a-7fe1e2f9f979 | -14.30492 | -52.00382 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30b2c178-fe29-3ecc-aab5-57af2d7f8628 | -13.7361 | -52.01904 | 2025-08-20 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6cbe92b3-e0f4-379d-becf-d4ee67d1c9f5 | -15.05111 | -54.83236 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5888d028-d108-38ae-afc7-971cd416993a | -13.14505 | -54.93863 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4b8d969-84d5-3293-8971-b8e6d4f2014a | -13.13333 | -57.15736 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 241505f8-007c-3f1d-8769-ba480aeeac45 | -13.74052 | -52.01481 | 2025-08-20 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffebf26d-1ed4-3a2a-b128-5e7b79f6317a | -15.00339 | -54.80535 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9268fd4f-851f-3709-90a7-41def5048b42 | -13.32985 | -54.4172 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 768a517b-42b1-31f4-8121-2a8bf05e580c | -12.97228 | -56.85081 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f0ce108-4307-3564-a202-5523d64d9b44 | -12.97272 | -56.8694 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07894c3d-b67c-369f-a185-5a5aa4e06e44 | -18.80105 | -52.60359 | 2025-08-20 04:59:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c3b630d-cd7e-315d-90b5-7946ff891bb5 | -15.05879 | -54.83725 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a94583b-2ad5-32ca-a7c2-c541e7dcd37f | -14.30871 | -52.00442 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08e5bb4e-d736-3132-bb0e-2aed9b60e8b0 | -12.97286 | -56.84721 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf8ca5d6-6bbd-303d-a392-5785cba3599c | -16.34456 | -50.17735 | 2025-08-20 04:59:00 | NOAA-20 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b00646c-f992-34ff-9f12-015da5f55907 | -15.00283 | -54.80906 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 274331c6-27a6-30dc-8611-5c567c5892ee | -15.02304 | -54.83529 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a22c245a-a077-3265-bb7a-2642d44e7550 | -13.32759 | -54.40931 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f1763a9-3c30-3d53-886e-2d3c6462ef2d | -17.66309 | -54.05796 | 2025-08-20 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c096d74-864b-3fa3-97a6-c64c905d64cb | -15.04886 | -54.82443 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71e28e90-43f7-34cc-ba0d-b0311b72d0e2 | -20.2174 | -44.13331 | 2025-08-20 04:59:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5a00c3e-6ffd-3574-934b-efab27adf764 | -18.67374 | -46.97961 | 2025-08-20 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c93faf1b-83bc-364f-896a-2b69691bc7fc | -15.64864 | -52.68387 | 2025-08-20 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af193fa2-9b4d-3f0c-b150-f8329e7654f4 | -12.98217 | -56.87473 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64fef1fa-b504-3c94-8946-6b2b3543987e | -15.00227 | -54.81276 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c30cec7-db8d-34ec-871e-f45aeea79513 | -15.52163 | -56.0695 | 2025-08-20 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a34cb126-3472-3f1c-9b5a-e8e6c5de6677 | -14.61843 | -54.92625 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f55bb317-44c3-33f6-bbcc-3c28b169a28c | -14.52863 | -53.25061 | 2025-08-20 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aec62b04-ce40-3e8e-b7d5-51b68aee054a | -14.65183 | -55.85755 | 2025-08-20 04:59:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9594f77-e4fc-3b58-892d-d8585bbcaf6d | -13.14005 | -57.1585 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d18d636-0d1c-3ae3-81be-c98b0ea4f063 | -13.18951 | -54.96047 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68a75d9d-73ce-3e3c-9537-b25c8dffde6e | -15.64359 | -56.30966 | 2025-08-20 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb64c5ab-d121-3c79-a615-7cc6264b4b3e | -14.64524 | -54.88553 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ba13c9a-db19-341c-9282-080650be6374 | -15.52219 | -56.06593 | 2025-08-20 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbdc3b76-69ae-3212-9659-8aa51694279b | -19.45453 | -47.19625 | 2025-08-20 04:59:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81304030-c9ac-3a35-b6b1-03733f6513cc | -12.96443 | -56.85691 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80c5ffb8-a8c3-3c7d-b456-f9a17afb702f | -14.88986 | -48.09245 | 2025-08-20 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b51a1ad0-7602-3312-85b7-2a46eb26fd3f | -15.63202 | -56.29672 | 2025-08-20 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f50baeb3-d88f-36de-96e1-3763ca686713 | -13.33883 | -54.40356 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac3cd05d-96b2-3651-8f0d-c60ff0860fbf | -19.86259 | -49.82283 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d92d7d2f-ebae-32a0-8f86-dc9c361126c4 | -15.90425 | -50.83938 | 2025-08-20 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 519eeef2-e41f-31a9-9781-b59e5bd63378 | -15.42779 | -46.72199 | 2025-08-20 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ea96703-b26b-30a7-815f-d1feb936f463 | -12.97446 | -56.85858 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92fba8c2-ed52-3c95-904c-e70bf0a37fb6 | -14.89214 | -48.08909 | 2025-08-20 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 730db44a-e836-33ef-b354-1fe0b84ff789 | -14.74372 | -46.29684 | 2025-08-20 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba45dd16-6890-3348-83d3-20a993c93a3a | -14.63851 | -54.88446 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0332a18b-3a4d-3388-b147-3ebcf6e8f0b0 | -13.03535 | -56.85789 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7a74cb6-6f8d-3229-94a3-968b6361a8f9 | -12.97432 | -56.88081 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e741a125-7ab2-3a67-8aa1-973f3d6bbeb7 | -12.97388 | -56.86219 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92963b6c-ae61-356b-be5d-994cd100e313 | -14.98486 | -54.81369 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcfa7fbb-b9f7-3d38-a077-b5e0da03ff88 | -13.15839 | -54.94078 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 417d131d-6d4b-34e8-b11e-8a29c105cd89 | -19.39531 | -49.61377 | 2025-08-20 04:59:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa092461-63d8-3720-9a93-5b9d66e79aad | -13.43808 | -57.09951 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68123ebc-6be9-35dc-8bdd-36211b546120 | -12.22209 | -64.23202 | 2025-08-20 04:59:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ef2ae69-7a97-3d39-8a36-bb9fa95c7c29 | -14.61618 | -54.9184 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcc6533f-069c-3c68-93f1-c8b5b1f255f9 | -17.63765 | -52.20081 | 2025-08-20 04:59:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7218e1a-e5e0-35d1-a51c-c7288f13a793 | -12.22658 | -64.23605 | 2025-08-20 04:59:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0cbf82-b2fe-3916-98da-b9d3702af74d | -14.99441 | -54.81905 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c312dfa5-13a0-3166-b37e-d8ff8664ff68 | -12.97112 | -56.85802 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73f08e76-7045-3691-be97-c420933f5fcf | -13.03594 | -56.85428 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aac7cc6b-f1b0-3d86-99ae-5b96b313c59c | -15.87235 | -50.65867 | 2025-08-20 04:59:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f55a43d5-2b7b-33e8-9b90-a052e2192cd6 | -15.6414 | -56.30196 | 2025-08-20 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9157184d-ea62-3df6-8c90-f4169a8629fc | -14.62451 | -54.88604 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d7784c4-128d-3130-a3a1-ecabc17c5ebf | -13.73573 | -52.01627 | 2025-08-20 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b00857e-8b9a-3366-8140-a9b65ee49c16 | -14.96217 | -50.12574 | 2025-08-20 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b980aad0-7f0a-324f-acab-d451f678658a | -13.15894 | -54.9372 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee795370-f491-3d06-850f-67344b9d23b3 | -12.9656 | -56.84971 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2aa24fa-a120-3535-979c-46f59274a43d | -12.96938 | -56.86884 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4248e2b3-f615-32de-849c-c9fd8b549aee | -19.87138 | -49.82932 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 40a798e8-1040-34c7-9906-55ce5678bd09 | -14.98711 | -54.82166 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8abe05d8-9426-32d8-ac6f-f3cd99eb80d6 | -13.15283 | -54.93254 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dd66196-ddc7-37ee-a1af-4abe0439efdd | -14.52925 | -53.25282 | 2025-08-20 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dd27a23-b400-3ac7-a78d-21d2db9f8cda | -12.96952 | -56.84666 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d3bb4a-3743-3f8d-8176-dbbd916e6379 | -15.00509 | -54.81701 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 686b65c9-30ba-3a64-88ee-0186235d73a1 | -13.33827 | -54.40725 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 535cdafa-3580-313e-8ed5-846aa01e7bdf | -17.67387 | -50.48393 | 2025-08-20 04:59:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3681b18-f97e-3be5-b19b-1e567c1e74b7 | -15.64415 | -56.30608 | 2025-08-20 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6c81a42-c15a-3d23-9d1e-533e4a37e3d3 | -12.97621 | -56.84777 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbb12f07-1680-371f-874c-1b0957aa35b9 | -13.14561 | -54.93505 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 10369e55-a573-3bca-bb19-daffc392589b | -18.52609 | -45.11258 | 2025-08-20 04:59:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d45045e3-2f29-3717-962d-cc018f8458ac | -12.9717 | -56.85441 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d21bc5f-1cf3-3586-b1b9-8d9ca588beb6 | -16.31189 | -50.1834 | 2025-08-20 04:59:00 | NOAA-20 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5fcd6d3-82fd-322a-a9c5-efd2c89ebd00 | -13.33267 | -54.4214 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README52.md)
