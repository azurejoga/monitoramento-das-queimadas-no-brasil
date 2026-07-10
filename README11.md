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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1738f8e2-cf0d-3264-80d5-426d3aceb296 | -10.85895 | -44.44082 | 2026-07-10 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9d01918-ea81-3843-8363-258fbcf7564b | -12.85007 | -58.31123 | 2026-07-10 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88389aa5-3a57-3736-8733-112cf60a03d1 | -13.27082 | -45.1526 | 2026-07-10 05:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59066598-1bbc-3094-8047-50efca8bd17e | -13.37408 | -54.37068 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3265735-ae29-3202-9671-ff19d705dc19 | -8.83318 | -48.33148 | 2026-07-10 05:10:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a08a7b9-cc58-3ae4-ad54-7da7ba6efdba | -13.30823 | -54.34504 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e248b5e-08a0-32b2-8b53-f5533018c8f3 | -11.28054 | -55.796 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a045b65a-5a52-39c6-a064-61d0b58d9e21 | -12.851 | -58.31038 | 2026-07-10 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b0acb22-2053-3e81-8e3a-8e457b6559d5 | -13.37351 | -54.3744 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67a1b528-8efd-3935-8efc-d9112c02b3a1 | -13.76336 | -46.26618 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a6da440-e86f-3fe9-ae7d-ec34631fd0e3 | -7.90709 | -55.42638 | 2026-07-10 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4b9c64-a7db-3a50-a93a-c07004561041 | -11.27446 | -55.79139 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9c728aa-2e10-3b5d-90d8-592c697f5dc8 | -12.49419 | -43.77571 | 2026-07-10 05:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2fb6c51-d297-37ad-8954-ad581b1382cc | -12.8478 | -44.35678 | 2026-07-10 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d564cf1f-5ce8-38ea-a5b9-b47002718011 | -10.4052 | -49.44638 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f839efbc-3d88-311a-8b60-65897061be30 | -11.17918 | -55.02535 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 242753bc-432a-3aa4-9052-86139b25c472 | -12.45197 | -49.58126 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e86cc949-4d75-3247-80cf-8c7f927c73ed | -11.46538 | -47.60585 | 2026-07-10 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9dd099b-76a8-3c64-be78-26b415d7cdaa | -14.55084 | -59.1523 | 2026-07-10 05:10:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e53d790-7bc9-33c3-8fcb-89c0dbe68e22 | -13.75607 | -46.2802 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0428415d-20eb-3973-8293-10ea988b4967 | -15.6658 | -56.0691 | 2026-07-10 05:12:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6dd9f64f-34dc-3d41-89cb-05d37f365455 | -18.02965 | -54.35716 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea70a9ca-40f0-3976-8894-3845f666ef16 | -19.60022 | -47.60725 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0f1698e-bb3b-35d6-a877-a2bd3b112f7a | -17.53387 | -54.00107 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f52231-0c92-350e-b05f-0d34c3ee8763 | -18.0261 | -54.35661 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dd01344-4731-3007-994a-ee1de29f1a90 | -19.59435 | -47.61218 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9da5cf6f-a390-33dd-a801-bafa261721ae | -17.54045 | -54.00633 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 737346f5-935e-3f4a-ad2b-42449040b2aa | -20.1539 | -54.40297 | 2026-07-10 05:12:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 123d510e-ad76-3aab-b106-8fbcd4399c07 | -19.58851 | -47.61337 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 775a1bc0-54c5-3ff0-b08a-009d890b024e | -17.53687 | -54.00578 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d77a304-b8b0-3880-89e0-d36e4fa1f83b | -17.54104 | -54.00216 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1575860f-21b5-3bfb-b10f-a9900e164943 | -18.02906 | -54.36132 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b18738c-3af8-3473-a615-9da1ad0af0a8 | -18.10135 | -54.0051 | 2026-07-10 05:12:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25457c92-0501-3b15-91d9-7174aaba2d9e | -19.66677 | -47.60798 | 2026-07-10 05:12:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68b8e420-70f7-3c7d-9aa4-67549f0ca1cb | -16.52861 | -47.74051 | 2026-07-10 05:12:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f045b7d-b2c4-34dc-907a-e1a41f75c88a | -17.53226 | -54.0028 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c0ddce7-1453-3977-b037-b20e7baccbfc | -18.02551 | -54.36076 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86c7ad57-89a5-3472-a45e-54fe5cd394f5 | -16.47144 | -49.76559 | 2026-07-10 05:12:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98046699-a667-3acd-8451-a6c087518cdf | -17.53804 | -53.99742 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1f33666-7b31-3a29-8602-0304eaefed7d | -21.08611 | -55.76959 | 2026-07-10 05:12:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1bafe85-9515-34e2-b980-d34119498de2 | -19.58847 | -47.6153 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df4ad189-0c4e-35a1-a5da-15ab6c5e528e | -19.594 | -47.61391 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75de9f22-4f68-317a-9a3d-edc24ad8bb31 | -19.66167 | -47.60362 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b06ffa8f-45f8-34a6-b7da-0e9870adfa10 | -21.09772 | -57.4682 | 2026-07-10 05:12:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64042b31-2ad5-3208-b8cd-a84526127def | -18.02197 | -54.36021 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9e029d7-6cc5-3ea5-b52b-44be0fb626a9 | -16.52898 | -47.73722 | 2026-07-10 05:12:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88445f02-14cb-35bc-a8ac-a59c84d4cb7b | -20.70276 | -50.5232 | 2026-07-10 05:12:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 460761bd-6c31-3faf-8d4a-1a17a44d7d3e | -17.99703 | -51.14533 | 2026-07-10 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f3b572c-2314-3609-8bab-5d95e3e68fbb | -17.53745 | -54.00161 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de9f6732-5109-37b5-87f4-b45529d7ddc2 | -19.59396 | -47.61589 | 2026-07-10 05:12:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 214583d8-6e0c-3ca3-b930-8815305382d9 | -20.18341 | -55.39733 | 2026-07-10 05:12:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2324311e-6bb3-39f8-9c71-0a237739b90a | -18.02788 | -54.3696 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1372e274-2554-3861-ab6f-18c73815a474 | -19.60061 | -47.60552 | 2026-07-10 05:12:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0121b9a9-4bfd-3ce4-84fe-fdcc02961e75 | -21.10106 | -57.46879 | 2026-07-10 05:12:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50599968-c2d7-39f8-a072-996214e99792 | -17.53328 | -54.00525 | 2026-07-10 05:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6665111-9ac2-3877-bd75-8b846bc8a3a7 | -18.02847 | -54.36547 | 2026-07-10 05:12:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0485a79e-9f10-3180-bd47-fcc91ea0a811 | -21.77009 | -56.30314 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d54e0514-5195-3fd1-9b69-87be4b57c145 | -28.83175 | -55.70539 | 2026-07-10 05:14:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| a8f82ff6-e4bb-3efd-b2fd-f1531d184c31 | -21.76326 | -56.30199 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a0d8a85-ffb8-3a11-b2f5-c24ecaf2735d | -21.76668 | -56.30257 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4569d6b6-e794-36e2-bf19-9822e5b59ce6 | -21.77865 | -56.29252 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9e95382-fe6e-3bb1-9c6b-ea923d330844 | -21.77067 | -56.29922 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1848bb84-96f3-3694-b489-3677aff13db6 | -22.91823 | -49.20716 | 2026-07-10 05:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 307358f7-6df2-3190-9d54-60ed80c4aa14 | -21.76725 | -56.29865 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a605c84-9840-3c15-bcb0-e139454016a1 | -21.76783 | -56.29473 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf84f240-508e-3cea-81c8-7a57d2787bbb | -21.76384 | -56.29808 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3eeca61-2d81-3c47-9497-12f73230165d | -21.76442 | -56.29416 | 2026-07-10 05:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c1fd99-34f5-343e-bf7e-d7186cbb80b8 | 1.98646 | -61.08707 | 2026-07-10 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2043f0f4-6a9b-3026-afd9-d061a26b1d00 | 0.75401 | -60.4536 | 2026-07-10 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 436862ac-33e4-3250-a5cc-2e92b02eea25 | 0.87655 | -59.70548 | 2026-07-10 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa450d6e-3df0-3e4f-8cd5-0927f8a5c254 | -4.15663 | -54.98639 | 2026-07-10 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7886d2bf-60d8-3f9e-ad20-fd317f86cf99 | -10.52966 | -61.17355 | 2026-07-10 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ada6337-c924-313e-9674-16c569249038 | -8.5056 | -48.06614 | 2026-07-10 05:27:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb2976ee-dda4-3220-bbd7-9317dfae9b7e | -6.43047 | -55.79958 | 2026-07-10 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 935bfb0b-b67d-3e45-8dc3-4b5abf3ba424 | -8.50638 | -48.05983 | 2026-07-10 05:27:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87a5241b-0130-35df-b720-3b2d2cb1e501 | -10.40133 | -49.44619 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6835594d-ec46-3c7f-9dad-d8a54f1f6feb | -6.42353 | -55.79145 | 2026-07-10 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95a09e8b-7073-3e84-b9ac-b66e394b07ff | -8.12895 | -47.87571 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 557af7bf-40f0-3318-afab-b24e7b93eb2f | -8.12973 | -47.86951 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9027e71-c4c8-3330-b869-8f6b5ea040bb | -11.49155 | -52.92205 | 2026-07-10 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c6f0a7f-ce41-3b6c-949a-3fb871abe909 | -8.13662 | -47.87039 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da2d163c-6611-3071-93f3-8d4c73795fb0 | -6.57076 | -55.14293 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad09304c-9c15-387f-aa3e-efe1b596cfc8 | -6.57018 | -55.14676 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f6b053a-bcdb-3c02-870e-9dc45f3cfe5f | -11.27952 | -55.79904 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f6dccaf-a285-3476-919d-be13fabd9389 | -9.40385 | -62.16415 | 2026-07-10 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 678c17b6-12a9-3be2-96bc-814097d272cd | -12.44991 | -49.58027 | 2026-07-10 05:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 249795f7-b12e-3ec8-90d5-ad841f76bf55 | -9.19062 | -58.06797 | 2026-07-10 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8829e116-beb1-3608-863c-46fa08e25a51 | -10.12963 | -50.18262 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f36e151-b3e4-362d-9585-38977d37f4b3 | -11.27581 | -55.79431 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b66a29c8-fb63-33bc-b74d-c7cf81f2ccda | -8.72206 | -47.84473 | 2026-07-10 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5854da8-91a0-3459-8b03-ab3c61345e98 | -8.71663 | -47.83509 | 2026-07-10 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b0539d6-03b1-30c7-9638-bfedfcac7c83 | -11.47529 | -52.9189 | 2026-07-10 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7b2829b-e5c5-356f-aa20-ab65b44c40bc | -6.55124 | -55.15938 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755a17d0-f3da-3c8f-b615-d0cbf4c273f2 | -12.451 | -49.57942 | 2026-07-10 05:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de8fb31b-5867-3e01-a848-7562dbeca6b8 | -10.40496 | -61.21107 | 2026-07-10 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5caeb959-b73c-3a78-9df4-a2675a8a3298 | -9.187 | -58.06744 | 2026-07-10 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11ab5f03-ecf3-32ff-8f78-f4d0fbb11e87 | -11.27266 | -55.78547 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a6e5e2b-81a6-3771-ae3b-fa023bf2c859 | -6.55598 | -55.15617 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 125709f4-13cd-3329-bda1-9d7cefb65974 | -10.12292 | -50.18664 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27f6ce50-f8d3-36d6-97b6-def099979083 | -10.40779 | -49.44685 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
