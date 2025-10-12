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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b326f815-718c-33d3-8802-399fd41cc877 | -15.86149 | -56.75628 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c36e8161-0e68-3cf6-bba3-c69dad0883f1 | -18.63504 | -47.88111 | 2025-10-12 04:46:00 | NPP-375D | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44606f4b-5f18-353f-b8cd-47dc5d0f138e | -18.45129 | -47.15511 | 2025-10-12 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83911a8e-0721-357b-9fde-b32e2039d002 | -23.51451 | -46.55286 | 2025-10-12 04:46:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e8e04455-8302-3132-ac22-bf5da7ecd811 | -19.04075 | -57.54187 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f506dc34-10fa-37d2-8091-f3b267e6ff02 | -17.81534 | -57.64307 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a7eda4a5-e87a-3568-ae40-5372d26a9027 | -15.28826 | -57.08258 | 2025-10-12 04:46:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e96571f-cba0-32a4-9ea4-affcbc4ec8d0 | -19.03576 | -57.54646 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f54987f4-20cf-312a-8470-66e1e94758b5 | -15.87346 | -56.75884 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d8548de-0f14-3d0d-b9fd-dca11cabf3ac | -15.87837 | -56.75962 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5120f630-d346-3895-80b7-c4addd5139c7 | -17.18925 | -46.96355 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cd6ca2b-098f-3fb5-b021-bdbe19ea982d | -17.54467 | -46.52508 | 2025-10-12 04:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f928412f-c9a4-3f90-a9ba-139b508d1468 | -17.36115 | -46.65926 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea86590a-72e1-3e5d-9047-28a1932ac1fc | -17.81513 | -57.66689 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 777e65e3-bc3f-3d2d-85d9-c8e857fb5fc9 | -15.46682 | -55.94717 | 2025-10-12 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 302eed6f-488a-38af-b742-151682d04005 | -15.85412 | -56.75113 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d10c0f41-9d4d-3492-b1be-4adf3573d81a | -22.05953 | -55.97969 | 2025-10-12 04:46:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 986c8101-024c-39dd-9791-a3505d1d83d3 | -15.85749 | -56.75546 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ad64c12-cd5c-35bb-a939-41afd5e64201 | -16.87266 | -51.36031 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a259f1b4-a56e-34d9-9a78-9426fd82cee0 | -19.09899 | -46.41455 | 2025-10-12 04:46:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbbbe366-2927-3433-ae1b-5a60cf85e564 | -15.28755 | -57.08639 | 2025-10-12 04:46:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a8217d9-f297-372c-adc5-0ef62d48b680 | -18.91001 | -47.01608 | 2025-10-12 04:46:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e54b32c-4b0b-3167-a43d-8d20a0d6a17a | -15.7788 | -56.54425 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec0b9890-c372-3b41-8bb1-b017a04d8690 | -15.28344 | -57.08558 | 2025-10-12 04:46:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b37804b5-275d-319f-b21f-76d3221d6b9b | -22.02065 | -57.11751 | 2025-10-12 04:46:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50b7a066-1aec-3574-abe7-dace8b3cd9e7 | -17.40913 | -46.86387 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcc35e14-31e7-3471-93bd-e51cf7c2f264 | -17.8729 | -45.03228 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bd400056-150b-32ff-a8d1-0f398672719d | -17.18994 | -46.95847 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20226ec0-69dd-3661-b375-29d922c094c4 | -17.54416 | -46.52895 | 2025-10-12 04:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1cade8a-8aae-3a24-8c55-2f603ec07954 | -15.86955 | -56.76248 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cbe2edb-7e7b-33dc-b4cc-ef6efc1477ef | -15.87354 | -56.76332 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af2a1ac7-2a46-315e-b1bb-f389a184134e | -15.86882 | -56.76162 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b5fa2b3-3ffb-3cd0-9bdb-4a1d6b77a0ef | -17.18525 | -46.96289 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76fcfde-f4e3-38e1-a447-c8c40ff2b2ee | -17.86848 | -45.02427 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f4a239b6-b66b-3785-bb77-c3ee71f8d8a4 | -18.6492 | -43.15086 | 2025-10-12 04:46:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18035e69-6f79-3a23-9b66-85d18d6babab | -17.86832 | -45.03161 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 643806aa-29bf-3a72-8d29-2df1d3215aaf | -15.28684 | -57.09023 | 2025-10-12 04:46:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01b218a7-3bbe-34ff-8e2e-e21502ca64e2 | -19.04473 | -57.54269 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 8a33e72c-02b6-34de-8afb-3229ab68bc9e | -22.33491 | -49.86808 | 2025-10-12 04:46:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 46d4b1ce-accd-3e2f-94ac-c9f24abb69e4 | -18.00427 | -52.39169 | 2025-10-12 04:46:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b967e329-63ba-3fee-bb71-fb0cdfe7942d | -22.33187 | -49.86304 | 2025-10-12 04:46:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d78002a3-d31f-32be-804f-8bf6bd93f31c | -14.93812 | -59.41394 | 2025-10-12 04:46:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64a573ae-65a5-3572-a0db-bf6025ac1f1f | -17.81995 | -57.66385 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 731a7560-9d94-384d-b835-33885dc1847e | -17.40405 | -46.87098 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fca1f50-9da3-3518-935e-cf50f4f36991 | -19.76381 | -42.42764 | 2025-10-12 04:46:00 | NPP-375D | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1c057221-661b-34e8-8886-0058e10bc394 | -18.90958 | -47.01419 | 2025-10-12 04:46:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cebfb535-c9b3-3330-a8c1-71c6e5834970 | -16.00385 | -56.00845 | 2025-10-12 04:46:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 851d5c3a-d6c8-3e28-8aa2-a1810f7a7b57 | -17.2105 | -47.65254 | 2025-10-12 04:46:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69372b02-fc03-31f3-a1ef-73fd14f3996a | -17.89868 | -57.66497 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 53feeae8-3c32-34f2-85a2-b1d9e078b62f | -19.82594 | -42.14364 | 2025-10-12 04:46:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9f20c9f7-2b90-3b2f-a741-a491b2f94268 | -19.7836 | -42.39915 | 2025-10-12 04:46:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 66d43f3e-2841-3852-af12-bc650c44e37f | -17.23825 | -46.71955 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee80df7b-922a-3b0e-b964-746891744023 | -15.87039 | -56.75796 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b345329d-8856-394a-9610-fa1a962dcd89 | -15.87438 | -56.75879 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 387ce831-c36b-370c-9f10-80116c6e3576 | -19.0288 | -57.5394 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8ac7d91b-1fcc-3f03-a444-328d015a4c58 | -15.87281 | -56.76248 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 599d9882-ab7c-3817-8751-3e4e778f9fb0 | -17.81523 | -57.62099 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8075d503-69e4-3917-b644-1c28b482f702 | -19.02084 | -57.53776 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1b871f77-ebe9-33f3-9b41-e5618ca62691 | -17.94795 | -57.62818 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7fb2b4ef-179e-356f-a0c7-d0f090131a41 | -19.82637 | -42.13927 | 2025-10-12 04:46:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e7e6d457-cb67-3f47-98a8-bc0a86a05452 | -18.5533 | -46.94335 | 2025-10-12 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9430fad-3686-34ea-9773-2318ac249b54 | -17.81836 | -57.67237 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c14b1454-6369-3b43-acf1-6ce910668380 | -19.05269 | -57.54433 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 069401ed-867b-3ffe-8471-5a88e0930073 | -15.29097 | -57.09105 | 2025-10-12 04:46:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1461d59f-f831-3b0a-a414-d1b8a927a9ff | -17.54518 | -46.5212 | 2025-10-12 04:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c962c9f2-818a-3623-a8c7-2fedc2d5300a | -18.15462 | -53.37379 | 2025-10-12 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85147978-57a9-3c2a-9100-d610077beb84 | -19.04373 | -57.54811 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 74abf1b9-bbb8-3033-9a1f-5e10de58042b | -18.55282 | -46.94708 | 2025-10-12 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b160aad5-b2bc-35ff-8693-a6d77a3840ff | -22.04109 | -55.16783 | 2025-10-12 04:46:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5be57e7f-510c-3808-9218-5b778fc7fbe9 | -17.8679 | -45.02925 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ef7d296a-210d-386a-9d43-6666ddc120cf | -17.25183 | -52.27463 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc16fddc-0fd7-371d-87e1-fbaa72e2f3cf | -22.29488 | -49.8892 | 2025-10-12 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d336d020-31e3-3e96-8db0-4701d2b5c6a6 | -18.64394 | -43.15021 | 2025-10-12 04:46:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eb848b0b-be84-38ea-9658-38f778b9e4a6 | -17.95414 | -57.61762 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 62c6cb1f-bb9e-3b4a-9949-c42235bddd5c | -19.78396 | -42.39545 | 2025-10-12 04:46:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd592cd9-c3c5-310a-aaf0-cb62e26d65cb | -19.02381 | -57.54398 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 51ebd748-43de-3dbe-a644-bc6871324be5 | -17.81466 | -57.64669 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aad22b4f-3a87-387b-8cdc-f3b1f4a5797f | -17.84571 | -57.66237 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4079743b-7073-3b8d-8548-bec5cf429a18 | -19.0995 | -46.41034 | 2025-10-12 04:46:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 160b58a5-005c-37a0-865f-5f91ab7aa557 | -17.845 | -57.66625 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f6ce7287-f245-36aa-985a-3306c6b7e9f1 | -19.02482 | -57.53857 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8f24ba73-463b-3af7-900a-7f0e33b568ee | -17.24907 | -52.27044 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1dd9a65-e69f-376f-aae0-e3dfd568fa09 | -19.09473 | -46.41389 | 2025-10-12 04:46:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a149d354-562a-3784-bb9f-4cf40efb5c65 | -17.81731 | -57.63251 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 889866e2-d637-3483-adc4-e28a6bfd23b6 | -19.04771 | -57.54893 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a4645ff7-36d4-3a7f-b500-2619051681cd | -17.81914 | -57.66816 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea7caece-6caf-3ecb-8f4e-250ae825301f | -19.76979 | -42.42435 | 2025-10-12 04:46:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b4c6eed-23d0-3397-a73b-1ead42378805 | -19.78435 | -42.39159 | 2025-10-12 04:46:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9068653b-521c-3bf7-bbec-b998491a6418 | -17.40148 | -46.85926 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6202fb63-756a-38bd-86a1-29e9f735fe36 | -15.8549 | -56.74679 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb56aff8-5df4-30d0-95bf-24dcf2fce6cd | -19.02185 | -57.53235 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 884ee565-23ad-3013-ae4e-c93c2f0a7223 | -19.03677 | -57.54103 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 40bdb61c-2a73-30db-a3a3-7cb57e1b4726 | -18.07583 | -57.52137 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e2245136-537b-3750-bba1-872574b04d36 | -19.05169 | -57.54975 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 7f621f2d-e296-3b5f-bc28-5f0ccd49dd63 | -20.21635 | -56.30337 | 2025-10-12 04:46:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2323aef-8339-33cf-a025-049f0016bd15 | -17.94459 | -57.6235 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6ffc8ab2-554a-3473-9dca-7c71c657d4a6 | -19.0964 | -46.41275 | 2025-10-12 04:46:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0896bcc0-acfc-3f26-a3c1-c7560d1d60bf | -19.0278 | -57.54481 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 41e478d0-8d2f-309c-ac36-f1abc11e77b8 | -20.56805 | -54.63232 | 2025-10-12 04:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69d9b289-f824-3f46-ae33-c872fcc47088 | -18.5574 | -46.94393 | 2025-10-12 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README37.md)
