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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb337add-477d-3d23-886a-cf485baa48dd | -4.43336 | -43.67926 | 2025-10-01 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ffaa19f-d197-3d69-ba68-71bf3d7e7bc3 | -6.07821 | -44.70317 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 235d58b7-7bbd-345a-b982-0824cbff47d9 | -6.28948 | -43.6632 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 261ca646-8944-3014-8ce8-6bbfe1e1f51d | -3.35199 | -39.85098 | 2025-10-01 11:57:00 | TERRA_M-M | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| c2f7eabc-d067-3c25-8f46-aa9c69e684b2 | -6.95211 | -41.11879 | 2025-10-01 11:57:00 | TERRA_M-M | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 68d73a23-9385-3d53-bb0f-01ab89cb8911 | -5.63244 | -43.91814 | 2025-10-01 11:57:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4baf8172-3081-30a8-84fd-42cd4a21c83f | -6.50125 | -44.27879 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 72acda0d-de6c-3917-b7a9-0bfbd9f2f55e | -7.30913 | -42.86812 | 2025-10-01 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e86bef11-7627-3b77-91c3-b132216894f5 | -6.1448 | -44.74119 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 23e21450-da77-36a8-ad76-5470f8a3e7a1 | -6.43205 | -43.06444 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f4636912-d6e5-3c8d-8ca8-15b88ce9a2b2 | -5.64175 | -43.91955 | 2025-10-01 11:57:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 2ef00dd7-9808-3ea8-aecc-41dc9ad9bb89 | -5.32934 | -43.72926 | 2025-10-01 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9263bf43-d38d-36a9-901b-375eae5f1cc7 | -6.30054 | -45.26602 | 2025-10-01 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8dfcbe42-e357-3818-be4e-cd2c6a5177f7 | -6.0515 | -42.44784 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0709b931-7270-3696-9975-510f30234d9a | -5.95748 | -45.85378 | 2025-10-01 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4e3ff84-c7c9-3b6a-8f7d-5a44631a990a | -5.32647 | -43.74882 | 2025-10-01 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6bbffe3a-7762-32df-a034-e432444a4a4d | -5.21791 | -44.83577 | 2025-10-01 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b7e01628-5dca-3333-89d4-877a5e82bd01 | -6.07864 | -44.34317 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 36b1c6ff-d020-3def-bb90-50e2dfa97a7b | -6.01933 | -43.79868 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 669caaa3-9c3e-3478-bba4-b1ea66bcb8ae | -6.05541 | -44.43463 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c0ae8bbe-0e61-3de5-b886-b851e65f7d6e | -6.79258 | -45.60407 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| efd200d6-91b0-3d6a-97c1-f0f8fa4d6607 | -5.4718 | -43.07077 | 2025-10-01 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e1b4fce5-b7b8-3ca5-9bfe-31ab8ff9595a | -6.06165 | -42.44022 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| f9a55bc7-637f-32a6-9a52-a700e57c7bd3 | -3.35068 | -39.86034 | 2025-10-01 11:57:00 | TERRA_M-M | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 59991bb5-1193-3094-b373-e620cefcf747 | -5.94272 | -43.31995 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 1d55c3c3-49be-360b-ac7c-b63159e03404 | -5.80909 | -43.73056 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6144fee4-d036-33e5-90d0-f7fe7435a3b9 | -6.01786 | -43.80853 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c23ca516-613b-32e5-8619-a8246c9fda02 | -6.29671 | -45.02194 | 2025-10-01 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b62bd499-3323-3c94-90b9-7beef02903ed | -3.80408 | -42.16646 | 2025-10-01 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 139.8 |
| d213c702-2200-329b-af41-a3e6c81430f1 | -6.53279 | -45.21821 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 02523b8b-4d86-3107-9866-de024ad07377 | -6.43074 | -43.07348 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0169d94f-ebe7-3ed5-b596-31ed1ea7fbc8 | -5.80375 | -43.07099 | 2025-10-01 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 6caf4144-4e60-3b17-b773-2ef7efa24b95 | -6.99991 | -43.78704 | 2025-10-01 11:57:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 5cdd3cb0-9ff9-3e0a-b303-e31dafd5e3a3 | -7.46969 | -46.46137 | 2025-10-01 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| edfd2d49-ec3a-3c98-b8ed-4ec8f83d1c67 | -3.67269 | -42.56389 | 2025-10-01 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 24f39ad2-c636-38ce-b9bb-2c1a605968b8 | -6.21595 | -44.23338 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| db0db764-0c82-37ae-8d93-6df015798cc6 | -6.97782 | -42.79602 | 2025-10-01 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 90bd32d5-5e81-3d1e-ba4d-9763221b8284 | -5.27538 | -42.77258 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 91e20dcb-0e34-337d-b0d5-5545707b29ab | -3.35972 | -43.19307 | 2025-10-01 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 57c06ea6-4e45-3d83-bcb6-f2dead49e4fc | -5.32012 | -42.77895 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 2d810719-4d66-3126-a0d5-8e0b83a28645 | -3.88145 | -42.52224 | 2025-10-01 11:57:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b2891689-c25b-3ef7-badd-9f6275805982 | -6.80109 | -44.73857 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| db485987-ab53-3cdc-9d6d-844760518daf | -7.63713 | -45.4408 | 2025-10-01 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bc687813-7f15-3966-a391-8134925e6fa2 | -6.56891 | -43.45315 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4858c1a9-3a91-3e33-8503-4b211b836901 | -4.95747 | -42.03242 | 2025-10-01 11:57:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 22dacb05-fcd5-3230-b27a-8206396dc515 | -5.33718 | -43.74034 | 2025-10-01 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3b9d62f2-823b-3e15-8466-dc11f1698cf8 | -2.93944 | -41.76616 | 2025-10-01 11:57:00 | TERRA_M-M | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c551677a-a7a8-328d-8c78-8c9adcd29d4f | -6.18805 | -43.90514 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f995290-8720-30c8-909e-1ba65b655590 | -6.10096 | -42.67953 | 2025-10-01 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| daedeade-3fdf-3113-bc47-9d8d7a7221aa | -3.80279 | -42.17537 | 2025-10-01 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7bb63dc5-5522-352c-a1cf-48ada7c80a5b | -7.63883 | -45.42959 | 2025-10-01 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8493b4fc-938c-35f4-833e-4c8fd4e66ae3 | -6.22203 | -44.23019 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d6526fe1-d92e-3135-98b0-0a2545af788f | -3.90434 | -40.18224 | 2025-10-01 11:57:00 | TERRA_M-M | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 76d9fd75-8023-386d-bad2-35bc8d12270e | -3.86024 | -40.42765 | 2025-10-01 11:57:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| c68802d0-6dba-39ee-90aa-241cbdb85ec1 | -6.02219 | -43.77943 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e1769bce-dc64-3b54-a56a-8ef31006b544 | -5.9412 | -45.89087 | 2025-10-01 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 606ea739-d308-39dd-b34d-60800f56d72d | -6.03141 | -43.78077 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a049d8fc-ff15-34a4-bcc7-a89748967142 | -6.23955 | -45.33333 | 2025-10-01 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1d2847e0-819b-301d-bf6d-3ac343ec0e60 | -6.29505 | -45.03288 | 2025-10-01 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1dc25579-00e5-39f2-9e1b-5fdcd4079c34 | -7.0013 | -43.77751 | 2025-10-01 11:57:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 85e625da-b35b-3440-a57a-4aaa11cab8cb | -5.94408 | -43.31064 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 155e705a-cfb2-3d39-a211-182f11a00078 | -6.32608 | -43.03374 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| efa9e40d-53ac-3b85-89eb-366c616f333d | -6.38775 | -43.86671 | 2025-10-01 11:57:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6d688363-ba02-363b-9f4a-d1d418eaddf1 | -5.83142 | -43.94904 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ae9393ae-eed6-33eb-ae92-53deaa68535d | -5.70676 | -42.65619 | 2025-10-01 11:57:00 | TERRA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 81ca99ce-8e15-3e08-933f-f097a173bdbd | -7.02836 | -44.45571 | 2025-10-01 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5e16e4eb-ae44-30e1-b6f2-2b6cffc50627 | -6.55304 | -43.93264 | 2025-10-01 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 42a2a40b-c246-3a37-b032-1c5fc0a303b9 | -6.53436 | -45.21279 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b684f203-b835-31bc-a883-4981023444a9 | -6.66429 | -41.39135 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 09eb5da1-bdb9-301c-8b22-8147a4207299 | -6.54254 | -45.2258 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 7ba6bb8b-351f-3749-a7f8-7559de697d80 | -5.38242 | -42.85915 | 2025-10-01 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d17f2aa2-4381-3edb-9630-a2590615c327 | -6.7227 | -44.58168 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e8be6e5b-20a7-35cd-8895-8f02952cd9c6 | -6.95083 | -41.12794 | 2025-10-01 11:57:00 | TERRA_M-M | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1e8bf04f-5b46-39ca-97af-9f94c10159d4 | -7.01252 | -45.50521 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 124f1eba-cd67-38c8-906e-89c34fb00681 | -6.49971 | -44.28905 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 45486f74-8d54-3df9-a9ca-690ab31d76a7 | -5.19514 | -43.57865 | 2025-10-01 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c7d274fd-bbf3-3699-af26-aecf2e898f19 | -6.55448 | -43.92297 | 2025-10-01 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| a7c93bb7-298a-338e-85a5-0eca77a236dd | -5.50324 | -42.72512 | 2025-10-01 11:57:00 | TERRA_M-M | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c788df70-b696-3ad7-b063-200631bfc727 | -6.28369 | -42.49298 | 2025-10-01 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0abe2da3-12bf-3274-a5ef-d6a999b8541b | -6.28484 | -44.06577 | 2025-10-01 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d505fb4b-cb57-33fa-b363-7c5ec880f02b | -3.68803 | -42.58464 | 2025-10-01 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| cff2e197-1843-3600-891b-91f234478586 | -7.02678 | -44.46614 | 2025-10-01 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 0bf76d22-6633-3fd2-9408-fd8337cf3c81 | -5.1554 | -43.72189 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b5b77d3d-9a04-3a24-aea6-099b4eec245f | -6.21448 | -44.24347 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 935ec819-f5c7-38e0-a3ee-ce6e9b00dd15 | -6.04264 | -42.4466 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 5d4e2370-4110-38f4-9df7-6208e46a2841 | -7.1447 | -47.28633 | 2025-10-01 11:57:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 43f51757-a146-3fcf-bbb6-c22b21402872 | -6.57027 | -43.44387 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 5ff6f84f-faea-35d8-a31c-8e6c2db41d01 | -6.29087 | -43.65368 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 656e39ca-1752-3fe1-b204-8b2ac48b8496 | -6.14288 | -44.7346 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b4122500-285d-3138-8f59-84f2486bc5a8 | -5.96419 | -45.88107 | 2025-10-01 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 77fae7c5-fbe3-3db2-8a3e-ae0d62d23e05 | -6.09908 | -43.13201 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2cc319e4-2f19-3fbe-b1b6-ff69b0029ab5 | -6.97911 | -42.78709 | 2025-10-01 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9e3466e0-f393-32a6-87e9-6415f712cbdb | -7.7868 | -42.50434 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| e861486d-e046-38df-a67f-dcf380c8302e | -6.08951 | -42.43509 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 886e8bbb-05f3-3c62-809b-99d6e8a6fb3e | -6.06361 | -42.67695 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| be78c430-398f-3422-954d-d1350e4ce624 | -5.81949 | -42.45089 | 2025-10-01 11:57:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b81d95e8-ac39-3cde-8963-f2571b0fa139 | -5.4904 | -42.75088 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| dd5c2e9b-52ac-3e05-8748-5729e4c9904b | -5.79847 | -43.7388 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 554b5b10-853e-3953-b2d0-8d9b65dd1d99 | -6.08193 | -42.42499 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| a955c1aa-83e7-3769-b65b-44481560e1a0 | -5.26964 | -43.19014 | 2025-10-01 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README141.md)
