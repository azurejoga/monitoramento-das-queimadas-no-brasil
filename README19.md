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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7477f7f-bf81-37eb-8bb0-c16d6a99bff0 | -13.85642 | -59.72356 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ee9f7cf-ca82-3a58-b0df-6ea3532fb8a3 | -9.4203 | -58.30308 | 2025-05-24 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de63d1f2-e913-3533-80f5-997eabb21461 | -9.96295 | -64.9376 | 2025-05-24 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f8d08f3-b5b7-308c-acee-6d16f2c73b07 | -11.76128 | -54.22571 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 508e6e41-ea38-3c0d-8779-b143a19e3a98 | -12.13987 | -54.66199 | 2025-05-24 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f1b4e03-3e15-309f-8e6f-9f55dff4f558 | -13.14572 | -56.81602 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f758b85a-16a9-30b8-bf7a-9f725162271f | -10.36722 | -57.50262 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5ca78667-e973-3b3a-a283-b2df75032c8b | -13.98358 | -56.01444 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb97632d-0fed-366b-ae6f-6eed25f1d4c2 | -13.15811 | -56.8176 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 548e71cd-6c71-323a-85d9-93720ec5efb0 | -14.02577 | -55.13436 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 312ced12-adf8-3c1e-83a4-4cf80bcd8f76 | -14.03251 | -55.13667 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4046e9a-4428-3c76-b274-44b4744a9f2d | -13.85161 | -59.71975 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 911b3515-34b5-337a-9b92-09a531339b03 | -13.82726 | -59.69354 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20a8169c-b4a4-396c-863c-57607fe40575 | -11.75762 | -54.22551 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 247767b2-90a3-3390-af13-97e847e046f1 | -10.68171 | -57.59868 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdb8bdcc-6fcc-30e3-b8cd-3f69985dfb93 | -13.37047 | -54.26215 | 2025-05-24 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| eb1a54a6-6e81-31af-9cd2-c3106a8d11b8 | -12.08873 | -57.37947 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70c8038-f59d-3b2e-ace7-72d72006b761 | -14.03893 | -55.14235 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a57d6d8-ddca-3a48-b2da-d1a6bb338020 | -13.86049 | -59.73357 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5edeb888-3abb-35f4-9cef-d0c7b10976d7 | -13.85605 | -59.72668 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb484d63-1022-3a68-a35e-67238b76578c | -9.23655 | -63.28614 | 2025-05-24 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0efa46af-3434-304c-8a28-f3aec91d49e2 | -13.15136 | -56.82173 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1392200-7ee7-3734-9643-2fd40483029f | -11.8956 | -62.90215 | 2025-05-24 05:48:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a892a5d-603d-3c47-bdc4-35b6d90a8292 | -14.03199 | -55.14182 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cafe56bf-f45d-3429-88da-795dab79bfe7 | -11.75413 | -54.22517 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f0f0ad7b-c9ed-38a8-be84-6527ba39b33a | -12.08927 | -57.37506 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22c99db4-d65c-36bd-80bd-6e74bf83a9e6 | -13.8616 | -59.72419 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdc8a4cc-a5ce-33dc-b075-4499ac1cf2f0 | -13.37185 | -54.26822 | 2025-05-24 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 97c5ed1e-e61b-39f7-8cd7-4287a38b5eab | -10.67894 | -57.60793 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57fbb05b-eb12-319e-a4b3-a00252bb3efb | -12.08697 | -57.38034 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aeca8532-5712-38a6-b309-0e9c38244ab4 | -13.82686 | -59.69675 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac9fd13d-5e1e-3ccb-bd02-770b71b4227a | -11.76053 | -54.23254 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe7af562-8202-375f-8b08-d18449a95a64 | -11.75338 | -54.23204 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33c6ecbe-40a6-3ef5-9dff-7e62279b50d3 | -13.85568 | -59.72978 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e8658ee-ec89-39ab-9a66-6b78952010d3 | -9.41984 | -58.30646 | 2025-05-24 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f91f6ba-1581-36d3-90a9-b64c5dad8ef4 | -14.0388 | -55.14386 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd1ec451-5cc2-344b-b32f-22ba3311cd15 | -10.67946 | -57.60382 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd4eb9e1-bf57-3ad3-a067-24b01cd65900 | -13.36464 | -54.26732 | 2025-05-24 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 05511aa5-9760-3af1-9caf-890dc8a00a13 | -13.86123 | -59.72733 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d51208d-8e5d-325b-b994-1174c744057f | -12.13912 | -54.66886 | 2025-05-24 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b37433cb-2226-3f5f-847e-3df4e1aeca04 | -14.01802 | -55.14169 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6ba226e-d079-32ac-b745-57b2b7aa05b3 | -11.99099 | -57.21288 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce048036-f9bc-3700-accf-e96f6b6cc4dd | -14.06412 | -57.11146 | 2025-05-24 05:48:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8ce6523-808f-31ee-baf3-655142c768de | -9.24037 | -63.2867 | 2025-05-24 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be0f763d-c793-396d-8e3d-07e01b0dc663 | -12.10535 | -64.05707 | 2025-05-24 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76af4b78-8a65-3c5f-9c52-95f348cf5efe | -11.99152 | -57.20851 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dac10322-38ae-3f14-af95-6b7f2384a787 | -14.0256 | -55.13583 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ea172b6-2c72-3bae-b073-b48e19409493 | -12.66746 | -58.21631 | 2025-05-24 05:48:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5d01d6b-5f10-3383-87f5-1c2e9d8c9046 | -12.08748 | -57.37592 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11ab1b4e-a8f1-354b-89af-20b5e1e5bb9f | -8.0889 | -43.1196 | 2025-05-24 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| a18bd23a-0b8e-3fb4-a5c5-14c1b97811f4 | -8.07 | -43.1216 | 2025-05-24 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| fd30b1f4-0463-364b-85e5-c780ddf71d8d | -20.94202 | -56.58942 | 2025-05-24 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 744270ea-6049-31f4-a2ac-aef3af8cdda0 | -20.94151 | -56.59567 | 2025-05-24 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a10ae33b-53e8-3662-a200-60cce6c0a866 | -15.62602 | -57.31187 | 2025-05-24 05:50:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59e1e3f1-bb1f-340f-8691-3510dae50d4e | -20.94265 | -56.59578 | 2025-05-24 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| abe7bacd-e991-3083-858c-547c60eaec67 | -21.96043 | -56.08204 | 2025-05-24 05:50:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f885cdb-9144-3e8c-b455-fd343388968d | -20.94947 | -56.59641 | 2025-05-24 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5f875c02-902a-32c6-afeb-9eb0378f2760 | -21.96086 | -56.0759 | 2025-05-24 05:50:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc893c0-275d-33c1-8399-16ded7d62367 | -15.6265 | -57.30726 | 2025-05-24 05:50:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5234dd5e-dbba-3853-842b-62306dee91fa | -20.94313 | -56.5895 | 2025-05-24 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f4c80fa3-091c-353e-a89c-5cdf94134364 | -8.07 | -43.1216 | 2025-05-24 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 38682f2b-bd00-304f-9e8a-dfcd2bbdd00b | -8.07 | -43.1216 | 2025-05-24 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| c948f9b1-b6d4-320e-be93-f5c0450e6c35 | -8.07 | -43.1216 | 2025-05-24 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 26a1ae1b-c8ec-3b77-a5b9-f94f181e871c | -4.28187 | -48.27412 | 2025-05-24 06:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 723c9359-7ad0-372b-99ae-71959da21fe3 | -4.28927 | -48.25795 | 2025-05-24 06:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 29dfa992-0d28-36ce-9845-a2c796340c37 | -4.28532 | -48.25014 | 2025-05-24 06:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 33481c57-a576-3451-a348-2fa3c4599b91 | -10.37038 | -57.50448 | 2025-05-24 06:22:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f68423c1-889c-3dff-92f2-956510d5d13a | -10.53512 | -55.71609 | 2025-05-24 06:22:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1ee3688a-faa2-3230-a968-8afa55b5807b | -4.28602 | -48.28179 | 2025-05-24 06:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 256a44bd-948e-3111-a314-71b29d70e2d7 | -14.06905 | -57.1041 | 2025-05-24 06:25:00 | AQUA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c4525568-5819-31cf-a7c2-026c5d7c7b2d | -13.36811 | -54.26591 | 2025-05-24 06:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e8e83441-4319-3d69-bb7b-c37c0ace6a9b | -13.15288 | -56.81005 | 2025-05-24 06:25:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 71a09713-e531-3d30-8529-e8eb036c759d | -14.03651 | -55.13486 | 2025-05-24 06:25:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 908821b8-d656-3e37-8872-f27b4c8a16a9 | -13.3697 | -54.25388 | 2025-05-24 06:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 79f3db2f-3777-384b-8f82-0c32cc8c409a | -13.85635 | -59.72287 | 2025-05-24 06:25:00 | AQUA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b386ff68-e482-339f-a29b-bb454d9cd6c8 | -13.14398 | -56.80873 | 2025-05-24 06:25:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8770e323-8c80-3012-82ac-784cf102c20e | -13.15153 | -56.81926 | 2025-05-24 06:25:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 75abb57a-9201-3e40-bcab-69367db77676 | -20.94024 | -56.59371 | 2025-05-24 06:25:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| dae86e80-25eb-3aeb-9bbf-2eda66bb376b | -13.37044 | -54.25955 | 2025-05-24 06:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a425cd96-f91e-39b1-9b4c-ae1499931081 | -12.40044 | -49.98403 | 2025-05-24 06:25:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6d062a97-2fff-3cde-aca5-5dbbc1c9fa62 | -13.98716 | -56.01282 | 2025-05-24 06:25:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 73f54fd7-a0a4-3f99-8a55-acd841bb68a7 | -13.19425 | -53.57647 | 2025-05-24 06:25:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ff54c05a-2ee7-3a13-a598-ace2002be88f | -12.08882 | -57.37603 | 2025-05-24 06:25:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94236113-47b3-3531-b113-0bebf93e9a8e | -13.18742 | -53.58347 | 2025-05-24 06:25:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6fef3955-a733-3c6d-aadb-ce7ce2724ff6 | -13.36878 | -54.27151 | 2025-05-24 06:25:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 5a4d0b28-3438-3e83-8818-f9dbdd4c56c2 | -20.94176 | -56.58233 | 2025-05-24 06:25:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 232f03e3-cba7-3b67-9535-11a154308c35 | -8.07 | -43.1216 | 2025-05-24 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 8887d186-840a-3f1a-92df-53997b00079a | -8.07 | -43.1216 | 2025-05-24 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| d3f5d763-a295-38c8-a054-c41fc452b8f8 | -6.5631 | -51.1126 | 2025-05-24 07:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f95ebe7b-8083-3926-b815-45a241cca1ad | -8.06501 | -43.11135 | 2025-05-24 11:42:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 13398d31-42af-39d9-a21e-fc38d2311ff5 | -8.07989 | -43.86869 | 2025-05-24 11:42:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| ed6005f4-81f1-33fd-9fbf-571a40117031 | -6.22241 | -43.35417 | 2025-05-24 11:42:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 3f2645b2-a2e8-3d26-af2c-62864a54522d | -8.07448 | -43.88873 | 2025-05-24 11:42:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 42.8 |
| c17461b6-d8bb-3c8a-8ea9-33caf09d268f | -8.07543 | -43.89515 | 2025-05-24 11:42:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 63ffa8c7-59d5-3bdf-b9d4-e654640b9fa5 | -12.05023 | -45.0869 | 2025-05-24 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6ee47313-cba5-3d5d-9e58-edf7f09b36b7 | -13.69285 | -45.24676 | 2025-05-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 0b72c863-4558-34cc-b6f5-676fb12ca53a | -16.34263 | -43.51421 | 2025-05-24 11:45:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b0d6079a-4738-3f43-9953-4a0df57a0d29 | -12.3706 | -49.981 | 2025-05-24 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| eaa91ad9-12e1-3a0b-954a-5c8269546e0b | -12.3898 | -49.9786 | 2025-05-24 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b366fec2-b3f1-38b4-8d10-323ae84aab98 | -12.3894 | -50.0002 | 2025-05-24 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |


[Clique aqui para ver as próximas entradas](README20.md)
