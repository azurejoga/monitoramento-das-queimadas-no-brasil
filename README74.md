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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd12b34-91a1-3aaa-8f70-262fb428231a | -19.66435 | -56.45177 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a35df16f-13b1-3c73-b149-2a44f74739d0 | -19.66352 | -56.4556 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9d0ca861-f4e2-3edf-bc1d-e4452ba35896 | -19.66268 | -56.45944 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 59626055-0185-3c88-ab38-4f45c19fb2af | -19.65802 | -56.45424 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| edd96bc3-2c52-3e2c-913c-e89bdb03f4ce | -19.65718 | -56.45808 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bfab50e3-e1fc-3540-a438-15b11fc22cc9 | -19.64407 | -56.49135 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6357f50e-2720-3220-b5e8-66862392c769 | -19.64323 | -56.4952 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0014453a-acb2-3d42-82dc-c689e5eeab53 | -19.63856 | -56.48999 | 2024-10-05 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e74ed3d0-6083-3024-918b-3f2874f72991 | -18.70146 | -57.29399 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ea3066c8-5d66-3c1b-b167-bd4d39ac1911 | -18.70045 | -57.2985 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 939dcd6a-a948-3e0f-992f-6a74f71dc56a | -18.67776 | -57.27592 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c39345ab-c6bf-3568-95d5-51c6bac41a5e | -18.67689 | -57.29268 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2fade295-19c2-3063-b6ce-2780782ceecf | -18.67677 | -57.28043 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 36d97c62-be58-3e07-9c64-65cdbb0940b7 | -17.13206 | -51.72159 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf5ad675-dfa1-381d-86c1-0d26deb1b6cf | -17.13124 | -51.72586 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6ba4d3e3-ec51-3905-9fbd-036987291035 | -17.13042 | -51.73015 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b948a114-5217-3031-8ba3-a478698009e3 | -17.1296 | -51.73442 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 385283da-70e3-3709-b66e-b69f86c41e5a | -17.12777 | -51.72068 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 804dfe87-6a53-316e-b93b-2e7e9d28603d | -17.12695 | -51.72497 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4c8d4da5-0b1b-3052-9702-60472ca5d311 | -15.17927 | -45.48197 | 2024-10-05 04:17:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c3a5028-015f-3ff4-8fdb-d5eadb4545f6 | -15.17869 | -45.48557 | 2024-10-05 04:17:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1797383-07e4-3707-9bcb-794bf25d2373 | -14.86583 | -45.13964 | 2024-10-05 04:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc53fe12-eb3e-335b-8bdd-9c821064e936 | -16.08008 | -50.24392 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5632ea0-4a6d-372e-a8f3-d1c9f199d8a5 | -16.07808 | -50.44115 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d852f94-b36a-30c3-8fe5-73487ca42dd2 | -16.0776 | -49.71548 | 2024-10-05 04:17:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd68a3dc-db79-36cb-a5b8-ec57a0f35bb1 | -16.07739 | -50.44489 | 2024-10-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f30bbaf-4cf5-3245-b65b-61468dd9ba5c | -16.07718 | -49.71343 | 2024-10-05 04:17:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 728e9cb4-9bad-3070-9eb8-e3998436298e | -18.59819 | -43.95195 | 2024-10-05 04:17:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef126867-a0ac-324b-9427-88604f0fa15e | -18.34206 | -44.01064 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f586d71a-7700-3ba0-ac4d-9fb2a52cb74c | -18.32505 | -44.03106 | 2024-10-05 04:17:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8065a208-34c3-336c-a451-ceb8eb7edcc7 | -18.32163 | -44.03056 | 2024-10-05 04:17:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eb36237-8759-35c0-b096-7cf314cf16fd | -18.12588 | -43.94224 | 2024-10-05 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3e3d703-b977-37cf-b5a9-2c99bb997801 | -17.69114 | -43.79721 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f92d73a-bd06-32ef-abe5-5b9e20cb820e | -17.68866 | -43.79311 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 61dfd1d1-988f-3dad-90f1-c1f6633c1e92 | -17.63798 | -44.31995 | 2024-10-05 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da953548-ad28-3dc1-8a15-1ff208a68c61 | -17.61666 | -43.26464 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1bcb2ece-d5aa-3164-90da-fa60fb108e97 | -17.33231 | -42.37172 | 2024-10-05 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79c87555-06c5-3510-bf6c-de0425a264ec | -17.31665 | -42.37807 | 2024-10-05 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9d24433-3878-3fdf-ab6b-73d4ed4c5eb2 | -16.44161 | -47.02105 | 2024-10-05 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1daec1eb-a6fb-350a-8eff-deca74cf56c5 | -16.4382 | -47.02048 | 2024-10-05 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 820c8cff-3b16-315a-925c-2eed37cb5f55 | -15.89138 | -46.88411 | 2024-10-05 04:17:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16805350-dd2f-356c-8823-8d230427190c | -15.88797 | -46.8835 | 2024-10-05 04:17:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58cb24ef-27bf-3208-a993-09908b1b8599 | -15.7095 | -47.8055 | 2024-10-05 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82f261d0-7ad4-3ae8-9d7f-8a73fe344ec5 | -15.66201 | -47.18997 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 922c33e4-e2b0-357c-bf01-d368b548a1d4 | -15.63815 | -47.1707 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 39b52d5f-dcb6-3ce5-ac85-c8066f28e24d | -15.63471 | -47.17009 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 436fc237-3904-3ade-9976-bbef8b3a2d9b | -15.24542 | -47.49162 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 347c59b8-8f0b-375c-994a-823430857d77 | -15.23428 | -47.49369 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48def356-6ca4-3adf-9e18-983fcd064353 | -15.23076 | -47.49321 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1df277a-d3fa-3ff4-b044-dbdae79b0a85 | -14.56143 | -49.29412 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 259952f6-4439-3c3e-b8fe-532082bfcfe0 | -17.12613 | -51.72928 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d58b0c16-618e-320b-b208-15f5d1bc45dd | -17.12532 | -51.73351 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1865a617-704b-3dde-9e33-6a4edeff0d3f | -17.12452 | -51.73769 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b7a1d88-67a2-3d1f-bd96-95988ffb7f1b | -17.12183 | -51.72843 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 37aa08cc-9b2e-3cf5-897f-375d30df6dad | -17.12103 | -51.73262 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d0b26fea-7993-33e2-9a9d-c7732e67a061 | -17.12024 | -51.73674 | 2024-10-05 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1963fe8-8a4c-36bb-9a59-ceadb6d788e4 | -18.10446 | -45.59507 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1487634b-f5f0-3894-8629-ee9b65f91073 | -18.10389 | -45.5987 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5780c6e-4c94-3a6e-8247-cc7a309285df | -18.1 | -45.60176 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8502eac-4af5-30d2-90cd-7f60b3be5c68 | -18.09572 | -43.95708 | 2024-10-05 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45789dcd-4a03-3037-b282-144f060e6987 | -17.77917 | -42.80915 | 2024-10-05 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e520bd4-a0b7-3db9-888f-58f2ca326390 | -17.74308 | -43.82501 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5dd3550f-8c7b-35f5-8b54-9badfb0a42d0 | -17.73966 | -43.82443 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| baaacffb-316f-3697-b5b2-40d414c10df1 | -18.69934 | -57.29085 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 446583c5-3bbf-32a4-a8b0-d29b0edc11fe | -18.69835 | -57.29538 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 686aba60-bf75-355b-81ce-cd990666d63a | -18.69759 | -57.28353 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8373f96d-a05a-3151-b1e9-0f441f0c83f7 | -18.69737 | -57.2999 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 238f7b00-ed71-3bf2-b44e-51748505f01d | -18.69658 | -57.28803 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0d65c919-dcc9-3398-b0ba-91f2eba09e10 | -18.69557 | -57.29254 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fb3692c7-5e24-33a0-aaf0-f1a9cf1fe0d3 | -18.69456 | -57.29705 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 600990d3-d44e-3e4a-924c-b7dfcef6963a | -18.69443 | -57.28486 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a34b9d38-edb5-354b-a4e8-db2864bd8635 | -18.69345 | -57.28938 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ec6235bf-be2c-3e44-a8ed-2cef4b8ebdfa | -18.69246 | -57.2939 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7104bdf3-f68d-3f4b-9d7d-7703881bc927 | -18.69171 | -57.28207 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| de61f665-d249-3c72-8760-d31d482f5ad1 | -18.6907 | -57.28657 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0e4ac4bc-c387-3a2a-a1d8-bbb7a2442739 | -18.68953 | -57.27885 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b5070814-2e89-3ddf-b80b-5460f1c12a91 | -18.68855 | -57.28338 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 87c9c0de-c1c5-3110-9778-fb0475c506df | -18.68684 | -57.2761 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 4d4cbf4b-20aa-32b3-afc6-97838dd88c68 | -18.68583 | -57.28059 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 313fb364-a27a-30c8-a695-961ba3d36544 | -18.68481 | -57.28511 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 49db3c2f-f960-3e8a-a7de-8d29a8bbcceb | -18.68365 | -57.27739 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 72ff7f28-2bbd-399b-8e54-f901e0907791 | -18.68278 | -57.29414 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| da29aed6-8a35-3a4c-bc88-23884b55c51a | -18.68266 | -57.28189 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fa6ba041-16e2-36e5-8cc7-206da685cf9b | -18.68095 | -57.27466 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 39007a94-2b37-3612-9d20-fed54f3f6a8e | -18.68069 | -57.29095 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 188ec942-0e85-319d-97a2-2ff370e41e6d | -18.67993 | -57.27916 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a989d005-5b82-3b17-bd00-8fd7189a4b41 | -18.6797 | -57.29549 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 164792fb-9a19-32fd-bdb5-d96856126611 | -18.67892 | -57.28365 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fbc8b10c-9bf0-3174-ac50-29a9bf1f6f44 | -18.67791 | -57.28816 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8788db8b-091c-3516-b8c0-e91885f37ef9 | -18.6748 | -57.28947 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ecdb3ab9-3380-39d6-9d2c-7b2d1ea9582d | -18.67405 | -57.2777 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 98d0c3e6-1fc6-3a01-8f14-cd0081e58e67 | -18.67303 | -57.2822 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 597093a0-b111-3411-be6b-22dde8242656 | -18.67201 | -57.28671 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| b8f8460e-65f1-328a-8a45-9d07d3544680 | -18.67188 | -57.27443 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 54ceb20c-44ca-36cd-bfd9-53cb40c45b03 | -18.67099 | -57.29123 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d57ae556-7fb6-3400-ac8a-d988480a1006 | -18.67089 | -57.27895 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| b41a6a0d-d5bf-3779-837d-15ab7400931e | -18.6699 | -57.28347 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1b9d95e6-c3e9-313f-839c-d74f36a1c3e5 | -18.66891 | -57.28799 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e58036a5-8b60-391b-a195-c89afbad6fad | -18.66816 | -57.27625 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| b71e6b81-3658-3a1b-95e0-11e5a04cd9ab | -18.66792 | -57.29252 | 2024-10-05 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README75.md)
