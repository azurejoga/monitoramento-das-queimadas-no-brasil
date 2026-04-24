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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 669f3d85-6372-3cbb-b395-f06ee56e0b3b | -18.27677 | -52.90157 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a225fa19-071e-3a70-994a-ddb016793464 | -12.09216 | -51.22868 | 2026-04-24 05:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd90c128-8b60-30b1-bd04-c81087471bc5 | -18.27275 | -52.8915 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 909ca7c9-0f55-31e0-bfa2-13bb9c5be1f3 | -18.27609 | -52.90776 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c2f7450e-95e8-3d81-a3fc-6636905c26fd | -13.71611 | -57.48188 | 2026-04-24 05:21:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c0d52ed-f1c0-3a90-b4d6-db7207298dac | -13.99413 | -56.64518 | 2026-04-24 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e338fdb5-7152-3d5c-8af2-5e288d0ddee8 | -14.20265 | -57.43103 | 2026-04-24 05:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad720325-8675-34d6-b44a-b48c90af5f21 | -16.42613 | -54.92272 | 2026-04-24 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de2a0c15-d6d7-30bf-a36e-4731657a3d28 | -18.27411 | -52.87904 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b994772f-e5a4-3973-a76f-c905daeb14eb | -18.27104 | -52.90704 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 24cc4815-6239-3b79-807f-0f10a7999bd6 | -12.55188 | -54.6117 | 2026-04-24 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a701fa20-8763-353c-83f8-fa523e13e759 | -11.84189 | -55.021 | 2026-04-24 05:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c0076c-edfb-31b7-b710-28d4b0ea71b2 | -18.28114 | -52.90847 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 813ea0fb-9ef4-311c-8fa9-abac22d6ad6f | -18.28653 | -52.90607 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd3b9392-0eec-37fc-bef8-7c1930950c11 | -18.2707 | -52.91013 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0da5bf6e-6623-30b8-9900-e6005bfb2ad1 | -18.27138 | -52.90394 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e575a4a7-c40b-3499-9886-a97af3182595 | -11.91528 | -58.06969 | 2026-04-24 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eba37f75-eb5d-39b8-9225-d583b85ff361 | -18.28216 | -52.8992 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efe2b16c-708b-38d2-bb12-3f89b94c9702 | -14.21107 | -57.42347 | 2026-04-24 05:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6309d1f3-e9a9-3dba-9ece-f13fc4c93d70 | -11.60459 | -55.32624 | 2026-04-24 05:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c4c484b-5eb0-3504-b029-aeb215688412 | -18.27711 | -52.89848 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3df2a556-37e0-353d-8f7a-9d0d0c51680b | -18.26736 | -52.89381 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2618663b-e018-3874-bd22-521e4ba94567 | -18.27814 | -52.88917 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50ddca44-860a-3acf-acb3-50fcc9056380 | -13.9935 | -56.64977 | 2026-04-24 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d72d2da-d449-3149-ae9f-9df84bc30c10 | -18.28148 | -52.90538 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1c3348fb-0af7-372a-bec8-9672cbd3bf7e | -18.27309 | -52.88838 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 730bef7a-2418-39f3-ae67-648bd2f561d8 | -18.27917 | -52.87984 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 059e7251-8933-31a4-ae5d-086323d437d3 | -16.4358 | -54.91564 | 2026-04-24 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d55e13b7-0a59-30cf-95f6-cc1ab458e6ca | -18.2724 | -52.89462 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a7581560-e14b-3437-b537-b962edfe663a | -18.23052 | -54.59355 | 2026-04-24 05:21:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88fc4b1f-74f2-30d5-ba23-327c3881e8ce | -12.99076 | -54.68164 | 2026-04-24 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd358062-68de-39c9-9e47-04ae1ee5a475 | -18.28422 | -52.8806 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d71f6a2-5c18-30bb-aa7c-eb4a650996ca | -18.28182 | -52.90229 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afea6da8-df71-3ab9-834a-6f4e3e8d811b | -18.26838 | -52.88448 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54a0751b-1513-3882-9446-30b118f941c1 | -13.98912 | -56.65379 | 2026-04-24 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c54d8b81-dd63-3318-b923-f4b8c76ce306 | -18.27172 | -52.90084 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 820d9a1a-23a9-3072-9c45-2300b4fd31e0 | -10.67925 | -59.36116 | 2026-04-24 05:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42fb2d0b-2121-322e-b4c9-101d452f1b9d | -12.34551 | -57.78623 | 2026-04-24 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5155412a-0ed3-3874-97f6-c1d5a4bb6e88 | -16.42664 | -54.91863 | 2026-04-24 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17f6c6d3-5e64-3817-952d-f7ae91680dd5 | -17.48494 | -51.08745 | 2026-04-24 05:21:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35921065-4cb2-3f6f-a9da-12fcad705780 | -14.20686 | -57.42724 | 2026-04-24 05:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 107c3b65-ab1f-37b7-b7fc-ff3ec767135e | -11.94146 | -58.08122 | 2026-04-24 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72eee5fb-65ab-388a-a468-f1db88fd7b02 | -16.42182 | -54.92209 | 2026-04-24 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f17e1463-7754-3cf4-bf9b-8f103bc3c2e0 | -16.42233 | -54.91803 | 2026-04-24 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2e6604b1-c9bc-3bce-936a-3d910966ab73 | -9.56494 | -62.46625 | 2026-04-24 05:21:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02f17fd3-5370-3170-9f15-9a17f145db6a | -18.27643 | -52.90467 | 2026-04-24 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| af0eb936-6eb6-3f0b-bb38-18c266561729 | -11.94433 | -58.08557 | 2026-04-24 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86341b8f-5a58-34be-b8e6-c02150445575 | -18.22753 | -54.5943 | 2026-04-24 05:21:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db71b099-dd52-3063-97ed-24982b2a5535 | -19.43327 | -56.61238 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 16eba250-401e-3211-a676-349d65d6bca3 | -19.45296 | -56.61898 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 7a2ea97f-d8fa-33d8-991f-b144b91de8fd | -20.72129 | -55.17435 | 2026-04-24 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f38a66b-4b29-3a5f-8b1f-7e7585d4fba8 | -19.10115 | -56.06207 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 56171677-5155-32d8-a1ca-c93096860a10 | -22.97125 | -52.69757 | 2026-04-24 05:23:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 64a84270-0d3e-3cfc-bb58-a4b643c224c8 | -19.09699 | -56.06147 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4f11a758-0a3d-3c9d-b845-3d7fd49fb213 | -19.44893 | -56.6184 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a3e33d43-d824-3f04-9369-e91c7ef326c6 | -20.71678 | -55.17387 | 2026-04-24 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c4b30ff-5c65-398d-9e6b-a3b050c411e2 | -22.97161 | -52.69371 | 2026-04-24 05:23:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4fe1554a-80fa-39f8-a2f0-b26c2b287d07 | -19.44603 | -56.57635 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 723d77e4-a49c-3fef-9041-2570852a6480 | -19.44199 | -56.57578 | 2026-04-24 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bcf8c9f5-01d9-3174-85cb-afde3881d39a | -18.2659 | -52.9016 | 2026-04-24 05:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 93ae054a-9cb2-33a1-967a-758c5130efb2 | -18.2858 | -52.8983 | 2026-04-24 05:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 39230c87-f16b-35c5-8ba5-06cf5e4f792e | -18.2854 | -52.92 | 2026-04-24 05:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 52b72678-31ea-3d42-8ab3-dd7016903e05 | -18.2654 | -52.9232 | 2026-04-24 05:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 74d694dd-78b9-36aa-91ac-bf246f85a778 | -18.2863 | -52.8767 | 2026-04-24 05:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| fddb05df-d118-35fa-a255-7670fdf6961c | -18.3053 | -52.9167 | 2026-04-24 05:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 896c5c3b-f263-3718-a7eb-a8d1ef61ecfa | -18.2858 | -52.8983 | 2026-04-24 05:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 2677ca2c-b11f-3c7d-85a0-b7eff7d2f874 | -18.2654 | -52.9232 | 2026-04-24 05:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 978692a5-5e48-323e-9a4c-13c6e9a944a4 | -18.2863 | -52.8767 | 2026-04-24 05:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| fcd80186-c4db-3034-a3d5-28d7e8e5e53d | -18.2854 | -52.92 | 2026-04-24 05:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 217.6 |
| c76ca4fd-4c13-3e47-a9df-e0f5d6cc64de | -18.2659 | -52.9016 | 2026-04-24 05:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 9bc259d0-792b-32f4-b5a8-ead44fb10a06 | -18.3053 | -52.9167 | 2026-04-24 05:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 2e421609-4dd4-3aef-95c0-6a5d538c1ccd | -18.2849 | -52.9416 | 2026-04-24 05:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 9b37613f-171a-3acf-94b6-d3472ab1e68b | -18.2654 | -52.9232 | 2026-04-24 05:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| d1574805-db7f-324f-9d76-22d5120b07d6 | -18.2854 | -52.92 | 2026-04-24 05:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 7d1d6384-ac9c-3248-a229-0520fd949d12 | -18.2659 | -52.9016 | 2026-04-24 05:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d3939887-8628-3c6c-be38-73c15fa67872 | -18.2858 | -52.8983 | 2026-04-24 05:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 188.7 |
| c6e3a18e-872b-38ab-842d-0271091c4915 | -13.7172 | -57.48502 | 2026-04-24 05:53:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d824b7bf-0a0a-3f2c-affa-c9a077e7acf1 | -11.91259 | -58.07209 | 2026-04-24 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42035964-69a3-30ed-89ff-79b3a8344d62 | -13.71764 | -57.48129 | 2026-04-24 05:53:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68af5161-f664-3995-ae18-238465a09b94 | -16.43371 | -54.91327 | 2026-04-24 05:53:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a633cf98-f0eb-3493-8fb5-f4ffb8616cb0 | -11.9149 | -58.07121 | 2026-04-24 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 833b738b-6930-357c-a4a0-a6dc2e03458f | -11.90975 | -58.0706 | 2026-04-24 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d030830c-d999-31f3-9b90-bec55129e309 | -16.42598 | -54.92365 | 2026-04-24 05:53:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a04657c5-dd71-3bb6-b9bd-5da4f6a90a17 | -16.41986 | -54.91746 | 2026-04-24 05:53:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a32283b-9a2f-3f4b-aac7-a74e6f05f97b | -13.71214 | -57.48066 | 2026-04-24 05:53:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0110d191-a7fb-3c86-8ed5-6447abe306e0 | -11.91414 | -58.07737 | 2026-04-24 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 945c5016-8109-33f1-b685-00dd6a926ab0 | -16.42651 | -54.91823 | 2026-04-24 05:53:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81519b67-c730-3cf0-b866-d7f95c9c8d25 | -18.2858 | -52.8983 | 2026-04-24 06:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 1a3f2e74-b203-350d-abc1-4d1d004c9e63 | -18.2854 | -52.92 | 2026-04-24 06:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.3 |
| c27cdb5c-5f04-3de2-8f4b-d3462200d715 | -18.2854 | -52.92 | 2026-04-24 06:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f48a9827-03be-3243-be91-ca44bd7153c9 | -18.3053 | -52.9167 | 2026-04-24 06:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 93057816-ad2c-3e26-ac98-f6fc36eddbca | -18.3058 | -52.8951 | 2026-04-24 06:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d62aabe3-7111-3c8a-848a-9c90e1a4f8bd | -18.2659 | -52.9016 | 2026-04-24 06:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 20a6f230-7442-3fc2-afed-b2b73d12ffc7 | -18.2854 | -52.92 | 2026-04-24 06:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 591ea694-60c7-3d06-af85-ed007a2d09ef | -18.2858 | -52.8983 | 2026-04-24 06:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 2a9d499c-3b0f-3011-b744-43261d62a11a | -18.2654 | -52.9232 | 2026-04-24 06:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 04fa7217-4a3f-31ab-b38c-8e30a88b4400 | -16.42106 | -54.92279 | 2026-04-24 06:57:00 | AQUA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ce9ab58d-2e44-37f9-9c1a-56caff102e5d | -16.42246 | -54.91296 | 2026-04-24 06:57:00 | AQUA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| debb9660-c2bc-3bfe-ad7f-720c32a3372f | -16.42246 | -54.91295 | 2026-04-24 06:57:00 | AQUA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9c7e0266-11d8-30ad-b071-4c8e4bb40bdf | -16.42106 | -54.92277 | 2026-04-24 06:57:00 | AQUA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README7.md)
