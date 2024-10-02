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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 615cba0d-28f2-3303-a5fc-dd396bc63dd0 | -22.38521 | -49.283 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 0497251c-3822-336a-861b-2b54867b00ea | -22.38474 | -49.28677 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 42606b25-fe6f-39d1-98eb-dbbab106947b | -22.38116 | -49.28237 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 6f0d1f56-59cc-3c71-8e3d-3dcad7ee561b | -22.38069 | -49.28609 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a0ac16ae-5efd-3056-8154-a5cc916dad0a | -22.3771 | -49.28173 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 11899119-80c0-3ba3-a573-5b2f79f05d4c | -22.37664 | -49.28545 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| fa38a1fa-3e85-3491-b717-1bbf4dc38953 | -22.37617 | -49.28925 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| bc2ca09d-6d61-38be-907f-f9c1e598af64 | -22.37305 | -49.28108 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 290ecfac-7722-333e-a87b-ea7b56f6c8b6 | -22.37258 | -49.28482 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 33b2728e-854d-3a68-ab27-f40c8f9dcaf0 | -22.37212 | -49.28859 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 5aa9261b-7ba5-3d3d-8c4d-07f2df09a2ad | -22.36899 | -49.28041 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c2bfa64-8083-345f-af49-eaced4888916 | -22.36853 | -49.28418 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 1cb497de-3ee2-3a05-92a9-cee5bd16a257 | -22.36806 | -49.28799 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ba8c271e-f6ea-3a92-b552-9ae971da91ad | -22.36495 | -49.27971 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 28dc2af8-b291-3f3e-831a-9b77637a3499 | -22.36448 | -49.28352 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| da65430d-5c31-39c6-88b3-12124108a3cf | -22.36089 | -49.27907 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3da32db8-b43c-3036-976a-a93a75012a9c | -22.60332 | -48.76989 | 2024-10-02 04:51:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58994bed-7c1d-3b1d-bce9-8ae9b247679f | -22.60283 | -48.77411 | 2024-10-02 04:51:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa6b2d29-c32c-3a93-ad8c-ee640e950333 | -22.54184 | -48.8135 | 2024-10-02 04:51:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdeff52b-2740-355f-9343-b91e40c27290 | -23.27876 | -49.72539 | 2024-10-02 04:51:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d476b88a-74b9-3e61-b2e4-67ce3cb43f65 | -23.17424 | -49.60071 | 2024-10-02 04:51:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c1978d20-e02a-3134-8e8d-ac6e71f096af | -23.17021 | -49.6002 | 2024-10-02 04:51:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8d97e9f0-6db6-3652-9efb-a9bf2e6413a8 | -23.16617 | -49.59967 | 2024-10-02 04:51:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 5b7f4642-3ebf-35d0-9334-2c8816519e08 | -23.15244 | -49.81097 | 2024-10-02 04:51:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6253b2cf-0336-3c6f-ae82-2dd28744946c | -22.99907 | -49.60691 | 2024-10-02 04:51:00 | NOAA-21 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1d780ee6-66a4-3fa7-adf1-0c2261ae1a25 | -22.40376 | -49.6703 | 2024-10-02 04:51:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 19c7203b-bc98-34fc-bb04-540be86f1896 | -25.21428 | -49.44134 | 2024-10-02 04:51:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d8e1d9f-fc60-310d-a121-dc8c488750fe | -25.21055 | -49.39943 | 2024-10-02 04:51:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 65e7f158-200b-3597-bbf0-086fb91bd059 | -25.20638 | -49.39857 | 2024-10-02 04:51:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6454a4f8-0bc4-31c9-b646-3afc5c512bb6 | -25.14459 | -49.33639 | 2024-10-02 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c3ae446-f98d-3478-a574-bf9c51546a08 | -25.03118 | -50.72003 | 2024-10-02 04:51:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9ac178a0-09a2-3e4a-888f-d1c29c683d11 | -25.02992 | -50.71859 | 2024-10-02 04:51:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3643affb-409a-3222-8d5c-756b52320799 | -25.02732 | -50.71941 | 2024-10-02 04:51:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d27e27c-4b0f-32f5-a750-9ceebf17201c | -24.60555 | -49.31769 | 2024-10-02 04:51:00 | NOAA-21 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a1c50853-bafa-3fb3-8b17-5accdb0c0e54 | -19.25857 | -50.89083 | 2024-10-02 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1484b36-9aaf-3bb1-b971-8eb4ddaa00a3 | -19.2688 | -50.84423 | 2024-10-02 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 91d0f89a-e290-36a8-8d1a-ba63340e76da | -19.26522 | -50.84369 | 2024-10-02 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e6865911-3792-3165-b6f7-c36f9d7d2429 | -18.89463 | -50.85695 | 2024-10-02 04:51:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c629c467-24bf-3acd-9e10-3fbc5f17987e | -18.87916 | -50.86337 | 2024-10-02 04:51:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6e7e5e7b-403a-32dc-be74-b055301bce24 | -18.87857 | -50.8676 | 2024-10-02 04:51:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c028922d-970f-319a-abc0-1c221fe1d429 | -18.87559 | -50.86283 | 2024-10-02 04:51:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b3fe20ff-5a26-394d-ac20-259c56d0c6f7 | -19.69744 | -51.10433 | 2024-10-02 04:51:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 01aa612d-554f-3576-b5d2-7dcfe0afaa74 | -23.53813 | -51.13272 | 2024-10-02 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 730b927d-7e0e-3cc2-8a44-0c0780d8dc5a | -23.53749 | -51.13754 | 2024-10-02 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7939e257-2a89-30c9-8441-b32c4b0b2026 | -23.53377 | -51.13704 | 2024-10-02 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 968bbca8-7656-3196-8e86-fc967dd8501c | -23.51222 | -51.09931 | 2024-10-02 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fba6024d-5a73-3732-8fcd-c6a6d55b0ed1 | -23.51159 | -51.10416 | 2024-10-02 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| befb4aa3-9ccb-3de3-b417-c99b1886d339 | -22.63418 | -51.53156 | 2024-10-02 04:51:00 | NOAA-21 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2bb7beee-5eeb-31da-bc99-d166a47357dd | -22.63357 | -51.53606 | 2024-10-02 04:51:00 | NOAA-21 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9ad58d7b-7d13-3d83-a044-be3589d8c2e5 | -22.62997 | -51.53549 | 2024-10-02 04:51:00 | NOAA-21 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10d9f32e-9465-3f45-b6f8-fd3e16107210 | -24.24469 | -50.74018 | 2024-10-02 04:51:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 063bbc50-cb05-36ca-b462-15c1a5c931f8 | -18.25295 | -50.82387 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb761e48-97c4-3b5b-8733-5e205270a1aa | -18.25058 | -50.81497 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 79e9d1b9-7c89-333e-99c4-78d18bfee894 | -18.24999 | -50.81919 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 664b5f06-ef61-32a0-a820-6dc1eea601d1 | -18.24939 | -50.82346 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20e5002a-e3e6-3b68-ba3b-8f7f66d36fc6 | -18.24879 | -50.82775 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86982f68-20ca-3017-82a4-9072d3af76c7 | -18.24701 | -50.81459 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 029467ef-aa99-33a7-8df8-ec61e0e9e260 | -18.24641 | -50.81883 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b01c9f0-0b78-343e-bf4e-8961799d6b94 | -18.24345 | -50.81417 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f890f5be-33b0-32a4-a137-9f4a4e532ab0 | -20.08754 | -51.33683 | 2024-10-02 04:51:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5197cd1e-e95c-3f75-ba0e-7611256787cf | -20.08695 | -51.34107 | 2024-10-02 04:51:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84516d83-9b35-30d1-8579-44c4d96f17a9 | -20.084 | -51.33629 | 2024-10-02 04:51:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25a62ba2-965c-31a8-8f7f-df51d181947e | -22.9169 | -53.11383 | 2024-10-02 04:51:00 | NOAA-21 | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0ea3f0e-0d52-3c15-8fe7-49a0fe93b17b | -21.3417 | -55.69066 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3bd01db-4001-3d4d-8806-c272fdd28cd0 | -17.68996 | -53.20765 | 2024-10-02 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b93b0e0e-4ab5-3793-a651-3c45beef03fb | -17.74972 | -53.19518 | 2024-10-02 04:51:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d84020d-a79b-3e92-83ef-390e41f8b8d3 | -17.74753 | -53.18738 | 2024-10-02 04:51:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b411351-8476-339f-ab06-2b99dbd296cd | -17.74697 | -53.191 | 2024-10-02 04:51:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b36c71b-bc4e-3d6a-a2d2-74bc960d958f | -17.74366 | -53.19044 | 2024-10-02 04:51:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 766ee113-7d87-3593-b745-7c247ba41340 | -18.60599 | -53.04261 | 2024-10-02 04:51:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ce1242-eda9-34a9-a4fd-f92dfc6a46bb | -18.60266 | -53.04206 | 2024-10-02 04:51:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07d037f2-663c-39b3-b5e9-cfe9023e2bf1 | -20.47681 | -53.6759 | 2024-10-02 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a0ff81b-e270-375a-8d9e-67e5a38f1af8 | -23.89091 | -54.21746 | 2024-10-02 04:51:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a0a7763-bb72-3bce-88bf-ba2735edc35a | -21.34108 | -55.69446 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22a4e9c8-681f-3dc4-a9d6-32f035dca3d5 | -21.34046 | -55.69826 | 2024-10-02 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee05a2b0-27b3-3192-aaa8-2120bcb5fe63 | -18.89412 | -54.50597 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01c3acb6-f983-3419-b19c-e62759a36aa9 | -18.89353 | -54.5096 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67f62777-7a1f-3ce6-a421-7008a8150dde | -18.8908 | -54.50539 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 30546a92-43c2-3854-8070-4f64783edce6 | -18.88964 | -54.51266 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 01f1a19d-5eac-3906-aa92-13a7252070ff | -18.88906 | -54.5163 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 96a9fcf3-df69-3a92-b7a8-1342bb0c9440 | -18.88847 | -54.51995 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22fcdefd-1204-3492-bd64-a697f65adf29 | -18.88749 | -54.50481 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73b2957a-c942-3d42-977c-0af201b3210b | -18.88691 | -54.50844 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4cd52d8-c34a-39e1-aaa9-fd4be062035a | -18.88534 | -54.49695 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 380cd05c-f143-3122-824f-f66dad2b8f65 | -18.88516 | -54.51936 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65d2cca5-fc07-30da-87a5-e33a44cdc292 | -18.88476 | -54.50058 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f0e492e-aab4-3093-ae5e-514ffff231c4 | -18.88418 | -54.50421 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cee27f1-95e0-372d-97b5-f211a653fe50 | -18.88262 | -54.49272 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39d4d63e-af3e-33de-9fde-f121c37ffdef | -18.88244 | -54.51511 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 98c7ea3b-b2d2-3982-ae7a-42e300cb698b | -18.88186 | -54.51875 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 550bee33-d136-3513-9f24-64afcbc2ab0d | -18.8793 | -54.49215 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc4f0030-b2dd-3b84-b19b-e5e396e267cf | -18.87872 | -54.49581 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 369da38e-5a60-3e7c-8899-92b8f950e026 | -18.87855 | -54.51815 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86cfb43e-08e6-3efb-9d79-a2569fd3c59a | -18.87658 | -54.48792 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 574d0a45-7113-31a3-973e-20f8d70c81c0 | -18.8754 | -54.49523 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bba1af5-6a35-31ef-904d-1c8d15eb3ff1 | -18.87523 | -54.51759 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c29c7d15-3bbc-32b3-9edd-2911688b53f4 | -18.8686 | -54.51647 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5d8993d-30ed-34b4-ada9-118f8219ce78 | -18.86801 | -54.52013 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bb222a7-e8ae-3a34-b836-2387594ea754 | -18.86469 | -54.51958 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02a40f54-3b5c-32d8-860a-4a91039b4265 | -18.86196 | -54.51535 | 2024-10-02 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README122.md)
