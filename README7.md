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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18313a86-0e3a-30a8-8a18-b786cd0ec40c | -8.22052 | -44.92347 | 2025-07-11 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 578edba5-03cb-3265-9249-9ea79f9c51ba | -7.48444 | -43.93238 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc2999a2-88aa-3156-b199-e50681b9aa46 | -8.89474 | -47.34758 | 2025-07-11 03:45:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d974bb3d-ad72-3bc6-b095-d35b761bf66c | -8.39214 | -46.93781 | 2025-07-11 03:45:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fe6bf66-e16a-3c5e-81bc-48fa260ab2a5 | -5.78738 | -45.11473 | 2025-07-11 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 967c9d21-e059-3ad7-97d1-66ee5d40e148 | -6.9955 | -44.45367 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c8e22ba-a52e-3b4e-9f0b-09781403f4fb | -8.36633 | -43.95589 | 2025-07-11 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52b6a7fa-aaa3-36e3-8e26-47b76d03dd76 | -4.22026 | -47.21143 | 2025-07-11 03:45:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7152c774-22e7-3a59-97f1-e79cc79e3f1e | -9.54028 | -46.29435 | 2025-07-11 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea706eb-c1ac-3945-8b4a-e61d14246232 | -7.55272 | -45.62914 | 2025-07-11 03:45:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6712c003-d1dc-3b48-a40d-a43f3e3fe582 | -7.94692 | -49.66261 | 2025-07-11 03:45:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6817ccfc-7d95-31a2-bb6e-ace839d8b344 | -3.78784 | -47.09599 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ab259f-d33a-3b58-863c-5661d913f84a | -3.75284 | -47.11767 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae6023d4-92df-38b3-be47-e920a93ff1ee | -6.67226 | -46.30117 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30f650bb-3a0f-33bd-adb9-d523e9750700 | -7.33501 | -44.32496 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26d9c30f-29db-3383-8b7e-b67b2b68b922 | -6.98901 | -44.45941 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6be0d26-0416-3772-9b5a-7a35faba9e92 | -6.44615 | -45.03423 | 2025-07-11 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ad83624-df5f-380b-a90a-b9fe801c2136 | -6.96028 | -42.72628 | 2025-07-11 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ced1180f-dc4b-33cb-9821-b864570ab01e | -7.32809 | -44.32709 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9603e50-adc7-302f-b138-cc5393aac819 | -5.4198 | -43.19129 | 2025-07-11 03:45:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc44b336-b82e-3b19-8430-e96c4d4d0d64 | -5.62353 | -44.26559 | 2025-07-11 03:45:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b96bd63-d22d-3b92-94be-99ffe1dc983e | -6.99983 | -44.44794 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bcdf09b-65de-385a-837a-1449e6600c0e | -7.20611 | -43.11767 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4fd53642-8737-3c82-8db0-ed2ba4c81908 | -7.18792 | -43.37576 | 2025-07-11 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e3f52dc-3550-3f01-9eea-8cec0cc563a0 | -7.1964 | -43.11596 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6b9834ab-feb2-3bf0-857c-7f54a360d99e | -6.99445 | -44.44727 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d85e1cb0-5ad8-30f8-9f1c-deb84259614e | -7.43359 | -43.83479 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99da65de-0e5b-3fd2-af9a-3244a5316492 | -6.85 | -42.7971 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86cb3bbc-3f7b-36fd-aec2-781e501d89ac | -7.42853 | -43.83382 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fbf7210-4399-330d-b783-9fe5ffd5a2fc | -7.19687 | -43.35421 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 43f8f8a2-236f-3fc3-b70a-da7e28733235 | -7.19156 | -43.11506 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d4673873-15c8-3611-8a46-c7c984c6dbfa | -6.45176 | -45.03508 | 2025-07-11 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b6d283c-e1be-30c0-9eaa-3b3830e27628 | -7.19094 | -43.35893 | 2025-07-11 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| be94fe4a-c206-365b-9a69-a4220d711522 | -6.55829 | -43.69287 | 2025-07-11 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bbf22bc6-a854-3f33-a4d4-fbaa8a876c41 | -6.9966 | -44.44737 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2af78b34-d45b-3637-8f90-7c446b9c0179 | -5.54365 | -43.90287 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d359e522-ea20-3593-9570-726feece118f | -5.91365 | -37.39436 | 2025-07-11 03:45:00 | NPP-375D | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eca41462-ad5c-37ac-96f9-8b3338252e5c | -6.99014 | -44.45292 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 188e4466-39fb-329a-9a3a-ff096708db53 | -4.5446 | -48.01505 | 2025-07-11 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2efaeee5-9a38-388c-8a5d-0c29ecace1c2 | -6.85476 | -42.79805 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 78791cd1-5d52-3a49-97dd-596e5efa8674 | -6.55885 | -43.68965 | 2025-07-11 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a00e321a-7163-3da9-a33f-9d4210bbe72d | -7.33397 | -44.32459 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239f547e-f5d6-31e1-b78f-b82ec9294932 | -8.37688 | -43.95506 | 2025-07-11 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23f9152d-24ff-38fd-81b1-7c8953b4772c | -6.15708 | -47.27724 | 2025-07-11 03:45:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3da9639f-4d76-3eb6-bfde-fa739d0489bd | -6.67666 | -46.30437 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d615e86a-9362-3ac4-84a2-2358701ea715 | -9.53455 | -46.29317 | 2025-07-11 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b959e968-fa1b-32ab-b170-213ab341e440 | -2.44233 | -47.47404 | 2025-07-11 03:45:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ac3382a-f74d-3918-a083-1e4e808a4a4c | -6.72466 | -44.33496 | 2025-07-11 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0e6fa8a2-6842-3369-8d50-0e0f721c1593 | -6.85515 | -42.79478 | 2025-07-11 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e68667d0-3fa8-3e89-b316-8e1b99fdbc6c | -6.99331 | -44.45353 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84e5efed-aad8-3bbe-9122-fae15c09937d | -3.75072 | -47.11263 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11012f04-375f-3c6d-9522-f4401e81f9f6 | -6.88668 | -44.06139 | 2025-07-11 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ab8faf9-a926-383c-baf3-d8690b3b4a99 | -7.3191 | -38.13931 | 2025-07-11 03:45:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e5b4cff-a68d-3398-ab4a-0a68a52c2056 | -7.19006 | -43.35741 | 2025-07-11 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6ef89439-ef5e-3b3a-a3e6-b0035c4a7534 | -6.81359 | -42.94463 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23615ba8-bde9-3f8d-a7f8-7a9335436372 | -6.85389 | -42.80313 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2ea92b3b-7c1b-38b2-9159-ac8ea13242cd | -5.4203 | -43.1884 | 2025-07-11 03:45:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f29c441-b9ca-3da4-ac01-f9918116fd11 | -3.75173 | -47.10693 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d325a08-10dd-3dc7-954b-9c4aeb8bac90 | -6.98795 | -44.45279 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b48c60c-5bd3-357d-b728-9a5d2210a695 | -6.67828 | -46.30233 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd7d5f7d-09cd-321c-8c80-1e51cc82ea0b | -7.49354 | -43.94053 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73e48290-5757-31a2-a786-7334336a7510 | -7.7013 | -43.57447 | 2025-07-11 03:45:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33c01373-197f-35aa-95c2-2910db78ed06 | -6.67585 | -46.30894 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 558ae926-8520-3ebc-acad-c682f247458f | -3.74616 | -47.11671 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16d8ac42-7a57-3134-a6d7-39376e7e6094 | -8.37188 | -43.95398 | 2025-07-11 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7f9d32e-f312-387c-9804-7d15ff97da89 | -6.15808 | -47.27184 | 2025-07-11 03:45:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7452cab-145e-3177-913b-61854c964c15 | -5.55005 | -43.89721 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60c5a59a-0bcd-34f6-8893-535d5257d0ec | -5.62891 | -44.26656 | 2025-07-11 03:45:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 972aa3b0-3b7b-3308-a410-961df429757e | -7.48899 | -43.93643 | 2025-07-11 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2a9ec6a-65e3-340f-8a46-5ba51f310df4 | -5.55061 | -43.89395 | 2025-07-11 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 130b87b7-698d-36fd-82cb-a59fe495d440 | -6.98677 | -44.45927 | 2025-07-11 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97aa1ce5-9d39-3321-8aba-87538159ac84 | -8.37315 | -43.95325 | 2025-07-11 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61a27a21-c3cd-3b0c-89ce-60c80661fcac | -4.55269 | -48.0098 | 2025-07-11 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0384b58f-5017-3e90-a523-f6fcce6d0937 | -8.37264 | -43.95613 | 2025-07-11 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e5b31be-76ec-35be-9651-b2af35a8b892 | -6.67142 | -46.30568 | 2025-07-11 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b07cf39e-ca20-3dbc-8ac3-60d8f581dcdf | -3.74811 | -47.10527 | 2025-07-11 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33de1590-5c46-3b89-a812-99a4c7ee0aa0 | -7.19548 | -43.12127 | 2025-07-11 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 4d7c84fd-804b-3114-b097-a81567e683a4 | -6.72997 | -44.3359 | 2025-07-11 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12476066-3dbc-3038-9952-3831aac7abd9 | -8.8895 | -47.34136 | 2025-07-11 03:45:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ed88da5-a007-3dd9-b00d-e1415462037f | -7.88019 | -44.55096 | 2025-07-11 03:45:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cef56c3-1938-3bdc-a97b-47fbe9d5a182 | -6.87448 | -45.23104 | 2025-07-11 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1e50e6e-d06d-3db4-819a-88efa52fd97c | -5.77946 | -45.11462 | 2025-07-11 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8f56f37-39ae-3ada-8368-071f2a52f111 | -7.65694 | -45.3458 | 2025-07-11 03:45:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d91d1f14-eb49-3c63-9084-0232a6ee4de0 | -7.11343 | -40.38714 | 2025-07-11 03:45:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f1c035ee-4674-3852-8a2e-4cdf8b942308 | -7.71958 | -41.3526 | 2025-07-11 03:45:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1bb02a47-7474-3690-ab12-d4d30b325a9b | -22.85798 | -42.97949 | 2025-07-11 03:47:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 648ae00d-70da-3fc0-9b24-bcc527d688e1 | -11.93372 | -49.30564 | 2025-07-11 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de192e5e-aaa7-3764-92c7-3928993bb463 | -11.90747 | -44.89701 | 2025-07-11 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| feb28a84-d994-35bc-838d-5aa4195de0bc | -11.84274 | -47.50559 | 2025-07-11 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87f7289a-d3cc-35dc-87bb-289ed1d7fcc7 | -10.62389 | -45.23218 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6df1c77a-ae46-3ec4-8498-c1ef2f99fc91 | -11.32683 | -45.22423 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f642736f-1a30-3566-8346-dcbd68169cbb | -10.58015 | -49.13455 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 092d244b-3fc2-341d-92ca-452289934c99 | -11.33382 | -45.21571 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b846add3-33b4-3093-b1c9-132b0960d055 | -12.9947 | -46.29863 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3f222c1-abc1-3c34-ba75-3bc8888a9f6e | -13.00096 | -44.85696 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a47d69ce-c675-3e76-8e6a-b42979f32a45 | -11.8377 | -47.49981 | 2025-07-11 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 113a744f-a6f3-3158-af13-fadd840d0fac | -10.68205 | -49.49944 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 07a2483e-6f11-38b5-b75b-3a3b9898f53a | -11.2661 | -44.8902 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd1e1ecf-182a-378c-b64e-e7e3c5d36ec0 | -13.16606 | -47.28805 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75393ebc-935d-3c4b-b43b-e0c6c45ee248 | -10.62065 | -45.22854 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README8.md)
