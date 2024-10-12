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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f775f311-42e1-35c0-88da-c63adfc1ea30 | -17.89047 | -57.32681 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c37e06cb-0b88-3939-ba47-45e292a46b73 | -17.88951 | -57.26567 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 5d7a341b-6b9b-3cdc-935b-bb2fb84255d1 | -17.88948 | -57.33476 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| da3bd5aa-bc5c-3fd9-99d9-9bba887870e3 | -17.88902 | -57.26969 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| e174f184-2a04-3a3b-88ee-e94fe8fdad77 | -17.88858 | -57.27531 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a2e4a674-c724-3af9-bc71-a2907c3654c2 | -17.88852 | -57.2737 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 750a11a9-bcca-3ff2-b30b-aa4632f1cf46 | -17.88803 | -57.27771 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7e566d31-efc8-3fef-8db2-9786da70fb64 | -17.88777 | -57.31426 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 062f3c83-92d3-31f3-b648-2fdf7d90a171 | -17.88727 | -57.31825 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 57088624-a061-3b83-b689-971244ed8a27 | -17.88628 | -57.32621 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 597f2403-b497-3352-8956-05d7205aa431 | -17.88578 | -57.3302 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1d64133d-3b03-3fbd-9478-90aa4a1509fa | -17.88529 | -57.33417 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ab620728-16b7-31f7-ac20-7c0b2817b4fe | -17.88407 | -57.30968 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 657605c8-2f38-3e92-aa86-c26369617c01 | -17.88387 | -57.3112 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| f91b2fc5-2baa-30f0-b4e1-bc63403d02e4 | -17.88382 | -57.27713 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b8deb20a-1cb4-39b6-9aaa-103452a07bc6 | -17.88357 | -57.31367 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| a90fdf11-6b15-3ad5-8ec6-d1d78189673d | -17.88209 | -57.32562 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 41fb32eb-7c45-3b2c-8a45-b5ccaa8d632d | -17.88178 | -57.3271 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 97335d92-8097-34bf-b151-a37aa3fcd5f7 | -17.88159 | -57.3296 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 835493d8-ea5e-384e-974a-466820b937ea | -17.8811 | -57.33358 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c5c540f2-26cf-35fe-bc73-4fe915bd97a3 | -17.87915 | -57.31459 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 496e7936-a7d4-3489-b3a4-ef2d56753354 | -17.87888 | -57.31706 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 266.8 |
| 57f98372-aa7f-3f08-9cf0-e2b2dfadfc29 | -17.87863 | -57.31857 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 35777821-8c1f-33aa-845d-8730de4a2272 | -17.87839 | -57.32104 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 80568d2d-1e96-3b56-bb41-4d52b15aa81d | -17.87811 | -57.32254 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1b416da7-e5ee-3112-9953-687b3147603a | -17.8779 | -57.32504 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5fa980e7-7241-3959-b70b-8ce4bb0f5c7c | -17.87759 | -57.32651 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1905a8b5-e300-3cd9-bcd7-5c0810f2b0e2 | -17.87616 | -57.30449 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 996237ce-6af1-3299-abf6-d44f092dc91a | -17.87567 | -57.3085 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| c74ceb27-ed72-30e2-b306-0178d615b159 | -17.87548 | -57.31004 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 0e8ef581-6879-3e0b-ba0c-9c64dbc7ad36 | -17.87496 | -57.31401 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.0 |
| a26c68a1-90ce-35cf-8547-09c8b04ea503 | -17.87469 | -57.31647 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 266.8 |
| 0499be7a-b198-3021-ac0a-40fd03ae5232 | -17.87444 | -57.31799 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.0 |
| c3b8cd8d-34a1-3d83-a3f1-d88b21175e12 | -17.8742 | -57.32046 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dac6325c-fd8f-30d3-9748-eac0a8f06e24 | -17.87392 | -57.32195 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 809f1bb2-4eec-3f4e-bcae-9d91b642a6f6 | -17.8737 | -57.32444 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c327f09a-ff94-36cb-9d73-e7a1ca91028b | -17.8734 | -57.32592 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8bf504f7-39a4-3c59-a942-a1acd29678e9 | -17.87321 | -57.32843 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d27edcac-fc95-3285-80b3-e976529c6805 | -17.87288 | -57.3299 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 59849d32-23bc-3d70-89fa-b11fb95256d0 | -17.87272 | -57.33241 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f7fcce27-3d63-3b32-8d92-1e5518c591da | -17.17652 | -57.44699 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 10d128b9-4837-3b96-95a3-429f6aa43417 | -17.07044 | -57.43685 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 78f29947-55a6-3283-88fb-1a0cbd9802b7 | -17.06945 | -57.44445 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8246b3d9-580e-3348-a673-f9075746f093 | -17.06534 | -57.44386 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d580439a-d88a-3309-a34f-05fb6fc0c966 | -17.0624 | -57.36954 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 23e3d326-d349-3a7f-a3a2-70a89b4611b5 | -17.0619 | -57.37338 | 2024-10-12 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f21deb23-eb43-3be1-a414-2001ffa82c42 | -16.99985 | -57.44732 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 50340a95-970f-3aab-88fd-c352bc892dbf | -16.99935 | -57.4511 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9381a4a4-d3e8-39e2-a24b-304172f083e2 | -16.99884 | -57.45488 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b0882903-4ddf-3b29-957d-fe124220a0d4 | -16.99783 | -57.46244 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 919f75d1-e9b5-3c02-b995-fc87b6e1d767 | -16.99733 | -57.46621 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 91bb0fc9-ad46-36c0-9c96-96af5182ea52 | -16.99682 | -57.46998 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4d4fbdf1-2422-30a6-b9e3-3c0c746ee3af | -16.99625 | -57.44295 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ca514304-e43c-3b33-ac4d-8f3e0b5b9333 | -16.99574 | -57.44674 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b4ec6e34-0961-3a07-9b62-bf35d87cf832 | -16.99373 | -57.46186 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 28b2102b-a3fd-35fc-a616-1fc887048465 | -16.99322 | -57.46563 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 76587c0f-20c6-3d63-97e5-12dfef3ba54f | -16.99272 | -57.4694 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| eede7fab-1163-37d8-9e5c-d215fa1045d7 | -16.99222 | -57.47318 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ddba5cf0-ef17-36a6-a6bf-e1363bf5f524 | -16.99214 | -57.44237 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8cb65e7d-ea4c-30b5-8c6a-a723259c2b2f | -16.99172 | -57.47694 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e086c3e1-f2ae-3d61-b31e-8224e55b41d9 | -16.99164 | -57.44615 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6342c7cd-e6ee-3b1d-bf5c-3fffc43a44ab | -16.98853 | -57.43799 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 58cc58d8-16ce-386c-9c6c-c6f866680dd2 | -16.98812 | -57.47259 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c8939bf6-0405-339d-ae4f-e10cc1693f77 | -17.84928 | -57.31448 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 7b93309d-48de-34b4-9abf-7b99817fa09f | -16.98803 | -57.44177 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b7d355c7-f757-3df0-9621-d75250be1277 | -16.98753 | -57.44556 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 18f6ab0c-8590-3257-9398-6a4a41c69408 | -16.98543 | -57.42981 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0106071f-1acc-33c3-b1f6-62a6013f52ad | -16.98492 | -57.43361 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cfb35bc5-63a3-31f5-8e5f-10c4a00402c7 | -16.98442 | -57.43742 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c5a72c70-26e9-3e20-97a5-2ac8554f24a7 | -16.98392 | -57.44119 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4d2eef90-559e-3667-81cc-038885f4558a | -16.98342 | -57.44498 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 88b17006-8404-325d-887f-df2f8c3f482c | -16.98251 | -57.48332 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 30374e05-df7c-3a0a-b66c-e58d128af529 | -16.98131 | -57.42924 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bb7885bc-c26d-33fc-8b61-b2697dc6921d | -16.9757 | -57.44003 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a40aabf6-faf0-3bca-bcba-c238512a6995 | -16.9752 | -57.44382 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 89672bcc-b55a-3cbd-a226-887833a18029 | -16.9747 | -57.44761 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9a5593eb-bb3b-3cfb-8b60-ad91a7cb8f5e | -16.97109 | -57.44323 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c22b4cb7-d3d2-388f-a180-770e5bfca4af | -16.9706 | -57.44701 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5599fe35-4b16-314c-a69b-7928f8c39719 | -16.9701 | -57.4508 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d52559a7-13be-3c84-b5b1-90071d515ff4 | -16.96364 | -57.49979 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5fff1e6b-263a-3985-af6e-9a31e703c5ae | -16.95976 | -57.43392 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 38d0ce50-f3f8-3443-a9dc-5a10f48e6ad0 | -16.95515 | -57.43712 | 2024-10-12 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0a6ab18f-1aee-3196-b353-cbeb884762a1 | -17.85296 | -57.31904 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| c71fd9fe-d385-3553-ad45-82a95b9e5ba5 | -17.85288 | -57.28661 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b0e32bab-e156-397f-9bec-10a3954738fa | -17.85245 | -57.32302 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| bca4690b-0ec1-3394-8968-67fa8a862ea2 | -17.85236 | -57.2906 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 206c2e03-bda9-3947-9b20-8c0eff8d5de4 | -17.85193 | -57.32699 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 2d1c5ce9-ae3e-3433-9dde-a42cb6ea3415 | -17.85185 | -57.29459 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a43e5d80-755f-3683-8ac9-2c9166c635df | -17.85142 | -57.33096 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| e5a41a6b-b487-32eb-bc07-1007c6e184f6 | -17.85134 | -57.29857 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cbfeb5f1-41b1-3032-9426-1ddce741c5ef | -17.85091 | -57.33492 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1ede8833-1eb7-38c3-8fd0-87d6cda4c652 | -17.85082 | -57.30256 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4c166d42-5bdb-3126-a888-b3aad8127aea | -17.85031 | -57.30653 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b83b1b16-a464-3af4-899f-2aaa58da0929 | -17.8498 | -57.3105 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 40290c79-ceff-347a-87e6-b89412358110 | -17.84877 | -57.31845 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5f16820c-2fdd-33d9-a560-09376ea0b2d2 | -17.84826 | -57.32243 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d908c8fb-2f40-3d73-893b-cf1cca955c73 | -17.84816 | -57.29002 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7c4d1f2b-cf7b-334d-8ef1-5b4ac359f686 | -17.84775 | -57.3264 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 62ce81ec-4355-36d2-b2c3-afd3331be88a | -17.84765 | -57.294 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b3233bd2-fe3c-38f5-ad93-18d3569d0b6d | -17.84714 | -57.29799 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README123.md)
