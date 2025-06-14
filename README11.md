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
| d989b984-6145-3521-8bd9-1d7dfa983085 | -9.39823 | -48.41955 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4e33fecf-ddc7-3649-9c0b-fed6ef71b5ff | -9.40254 | -48.42945 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf01b585-d625-3717-bb0e-d9aa36294ac7 | -10.85384 | -46.71149 | 2025-06-14 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e46239eb-ad7b-38d8-b3c9-e3386c1f80f5 | -12.59914 | -47.06781 | 2025-06-14 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e596cff3-9d38-3ffd-8725-719084fcaa4c | -9.39902 | -48.41528 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32029dd1-6943-3e28-ade8-33304ddb16ba | -15.9093 | -42.65586 | 2025-06-14 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cdd7aa63-6a85-3bde-a84b-70b0d115da94 | -16.19741 | -46.46743 | 2025-06-14 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| bf769469-2431-30b3-a1d5-b19133da22db | -15.99035 | -49.82171 | 2025-06-14 03:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8da29e7b-60c0-3c86-83dd-31b569bc33fc | -14.66834 | -53.39482 | 2025-06-14 03:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dbb2ee7-2af6-329a-868e-1d69202f18da | -9.40576 | -48.41219 | 2025-06-14 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1014f33-cf77-3bc8-81f4-5b5191c790bc | -14.6891 | -53.37499 | 2025-06-14 03:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f752f0f-9700-3f6b-9c7f-e806508f9e38 | -12.27232 | -44.60382 | 2025-06-14 03:51:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a78c4584-f1ab-3bd7-aa2c-70e99b62a5b8 | -14.68053 | -53.37427 | 2025-06-14 03:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0108d381-dcf3-324d-98a5-79db736b4ec0 | -11.89701 | -47.46459 | 2025-06-14 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2b8ec09-7cad-364d-9ba9-4b6af14aecf2 | -12.59327 | -47.07052 | 2025-06-14 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1acec3cc-8a91-3b4d-9bdb-372ff3d8e0e4 | -8.92256 | -49.84691 | 2025-06-14 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 992d12cd-ea86-3581-8ed1-177e9ded8093 | -13.22578 | -49.8362 | 2025-06-14 03:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e226c74-b5bc-3057-8891-d46d3bf9968d | -10.65663 | -44.48632 | 2025-06-14 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32eb72bb-0f60-364b-a225-cbd165372465 | -22.903 | -43.75281 | 2025-06-14 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9fa50c18-c565-3037-9db9-0e1a394ddf0e | -21.63271 | -45.8474 | 2025-06-14 03:53:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f7bf5f5-c375-37d9-a473-acc196891514 | -20.83777 | -45.45316 | 2025-06-14 03:53:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fecbc6ce-f141-3850-98b4-d0c2163fdecf | -21.62867 | -45.8465 | 2025-06-14 03:53:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6c09deba-76d6-3614-84d2-f6eb1e1ab6bf | -22.90223 | -43.75716 | 2025-06-14 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04d83d3b-a008-3980-b588-66215826b6a5 | -21.44135 | -54.57504 | 2025-06-14 03:53:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 86616e53-6b56-369d-9943-61c257c2bcc7 | -16.78476 | -49.11489 | 2025-06-14 03:53:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cdcf5df-14d9-3687-8d02-2d4ec8132227 | -20.31202 | -45.58541 | 2025-06-14 03:53:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29f69583-b22c-3c0c-918c-a10188222533 | -21.42538 | -48.64516 | 2025-06-14 03:53:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e9b03e1-5ae1-3e56-9ce7-b3ae0af0f3a1 | -17.64454 | -47.45588 | 2025-06-14 03:53:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 356e6610-e414-3fe9-844e-79dc9738947a | -22.85721 | -42.98182 | 2025-06-14 03:53:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b1e6fd93-1f3c-3475-8965-ceb61b271a36 | -16.72357 | -49.08144 | 2025-06-14 03:53:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10dd8407-e1db-3acc-b90b-59e3801373bc | -19.03663 | -47.91203 | 2025-06-14 03:53:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7698df7c-0e38-31f9-8567-5cc5808c409d | -22.50508 | -44.56727 | 2025-06-14 03:53:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8f815dc1-c214-321c-a397-d728d459aec2 | -17.98465 | -44.26371 | 2025-06-14 03:53:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f456f4f2-e139-35f8-a6de-298814009eb1 | -19.52116 | -46.09042 | 2025-06-14 03:53:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66c21afa-1b89-3f09-9df1-050e07d97084 | -16.78489 | -49.11415 | 2025-06-14 03:53:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 485a8ae8-5a2b-3576-9949-f728d6742097 | -16.7243 | -49.07795 | 2025-06-14 03:53:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b809a1e-17dd-3772-9ecc-6dc13478c7f1 | -21.40237 | -44.27175 | 2025-06-14 03:53:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64000180-bba6-3cc4-bce6-31cc8ba04bba | -23.40774 | -46.5567 | 2025-06-14 03:53:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 79326fb3-45db-3a90-a0f9-91c4e046e077 | -17.58173 | -47.49362 | 2025-06-14 03:53:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e434869-c142-3d98-816f-115bb8d3045d | -23.33828 | -46.77217 | 2025-06-14 03:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9bde2063-6264-3ceb-9d09-7579e0a09185 | -22.78633 | -43.75769 | 2025-06-14 03:53:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db2f4066-aa92-3116-bb15-cc4a8aad7b46 | -16.7841 | -49.11798 | 2025-06-14 03:53:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bb2876b-488a-39f5-bed7-8612ca7f804e | -23.14909 | -47.15894 | 2025-06-14 03:53:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a9ccf2ab-cdd9-34cc-a060-3be22d1d1543 | -20.41822 | -43.55322 | 2025-06-14 03:53:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a11574f-7837-3eeb-9393-0cc6d64b37af | -20.60828 | -48.86688 | 2025-06-14 03:53:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d82041c3-f05c-3cb5-8b8d-06b3a66859ca | -22.85568 | -42.98277 | 2025-06-14 03:53:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0a8905f3-e30d-3876-aa9c-a1b2df12898e | -19.45327 | -45.30565 | 2025-06-14 03:53:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12d4be59-ea51-3f35-9bdb-7bb54f8c0710 | -22.67629 | -42.85509 | 2025-06-14 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae7dc706-fed5-3a60-a2db-43d83988bcef | -22.35275 | -41.99896 | 2025-06-14 03:53:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4200b2ac-e556-3e4f-ad02-9f91f5dee024 | -17.9807 | -44.26315 | 2025-06-14 03:53:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bab34d06-d568-39a2-ac02-1b56f459de52 | -23.62602 | -46.49738 | 2025-06-14 03:55:00 | NPP-375D | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43353818-042a-3960-9d38-1efbf3b9adec | -29.72478 | -51.1212 | 2025-06-14 03:55:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 00061bad-5a63-3bdb-a3ad-d6724196b847 | -6.9602 | -42.9052 | 2025-06-14 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 12fa11d3-6be6-3ae0-87fa-e8a069aae497 | -6.9605 | -42.8816 | 2025-06-14 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 70ebb921-0ba2-3b2d-81b2-161481e8505a | -14.2121 | -57.4098 | 2025-06-14 04:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6e7d3f8e-126e-32e1-bc4f-19ab6ac2e175 | -13.9062 | -54.6084 | 2025-06-14 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0e621c59-5f2e-3bdd-bb42-2eccf84d5b5e | -21.452 | -54.5675 | 2025-06-14 04:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ad8d4604-95a0-3927-8c2d-1e5b7a050337 | -10.9355 | -56.8322 | 2025-06-14 04:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7243e1f5-f245-31fb-b5dc-fc50828b8a56 | -6.9602 | -42.9052 | 2025-06-14 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 99b7a065-dd14-35c6-aa08-3143c7a1d821 | -13.887 | -54.6106 | 2025-06-14 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 391fa43c-1ad1-3e7b-8622-cb3d5e10c13f | -6.9605 | -42.8816 | 2025-06-14 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 5071def0-24e5-3ac4-93e2-af3ca352c832 | -14.2121 | -57.4098 | 2025-06-14 04:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 0df168e5-e45e-31f0-9808-cd096fa4be9d | -13.9062 | -54.6084 | 2025-06-14 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 08536e8c-5516-3ccb-a1c0-cb2122e1cfb5 | -6.21476 | -43.3272 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 173bed83-f254-3f57-978e-9c70e7b42312 | -7.18872 | -43.5497 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2a19cac-dde9-3b55-b7be-0623edc9ab59 | -7.6382 | -43.67168 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b2e1892-de2b-3eb7-a05d-a04ce8856178 | -7.18487 | -43.55264 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e2a63c8-f92c-3cdb-ae55-69644f4577b6 | -5.91507 | -43.46098 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c58b9d2a-0062-308b-b590-67618e83817f | -7.21006 | -44.73074 | 2025-06-14 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e1fc23-8d32-3b80-bc8d-cd79c3434e8b | -6.21422 | -43.33066 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c968aeab-76a4-3856-9dbb-21c40a616db3 | -6.94303 | -42.80134 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d927c5dc-c776-3828-88f2-0767ca8d88cc | -5.44875 | -44.8166 | 2025-06-14 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a86cd81c-2bdb-32a0-8790-f866bbd690b6 | -8.20766 | -42.83644 | 2025-06-14 04:12:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 396d5628-a643-3b39-92a5-441ce770df8f | -6.5634 | -43.42214 | 2025-06-14 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9289dbd-bc48-33eb-ba0e-e9552770d7b4 | -7.22404 | -43.58372 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7adf05d1-e327-3739-85c0-4ff834e2d63a | -5.7742 | -43.47032 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d89a4541-4e26-30f8-8637-aba7661dfacf | -7.67677 | -43.64225 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bfc378b-e4f1-391f-b576-fcf19815ec96 | -5.32615 | -44.96603 | 2025-06-14 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d90be843-4c08-37a9-8178-ac95653511c8 | -7.63156 | -43.62794 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 329b8623-3633-39be-8900-868b43784a4b | -7.10727 | -43.44117 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b83556b-dfdc-3b66-bee8-fe705632cfde | -6.94818 | -42.89801 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1e812e42-fe19-36fb-99cc-745c91b939c1 | -7.11058 | -43.44169 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57da5f07-a768-339a-85f3-110e7c4d3e99 | -7.3986 | -43.91829 | 2025-06-14 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64e92931-8c84-3fa1-b74d-30e020ef71eb | -7.23238 | -43.09922 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 17d10586-e29e-398a-b712-a8138698ada4 | -6.33548 | -43.74491 | 2025-06-14 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 602c87c4-2d83-3a30-a1c7-331a8c2e04c9 | -7.22694 | -44.73338 | 2025-06-14 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1ed83ad-d771-30d7-b808-dd92b7b7ad72 | -6.60756 | -43.89184 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ba6d2a89-54c2-3962-83b7-0e7eb7589e41 | -7.48804 | -45.46021 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51b09115-6d3a-334c-8aaa-dc5366cfce6c | -6.60256 | -43.90179 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 74e16ee6-d684-32a8-819b-9b23d77cc211 | -6.94965 | -42.80238 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 19ea4230-5bd0-3c19-8c4c-962f3f5be2bf | -7.45309 | -45.50116 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 964a8176-123b-37e3-a8c6-b4e3a8761b31 | -8.0723 | -43.11493 | 2025-06-14 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 2d61bd31-221e-3199-a98b-292717e21c47 | -6.95322 | -42.88821 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| df821a4a-6f23-3a38-b15d-c0c020bf5348 | -6.67955 | -43.76026 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 377b4809-aca7-3f1a-ac78-2f8051cb4605 | -6.60312 | -43.89829 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a774431d-bf85-3f43-b20a-f6e74c9c0dc6 | -7.07539 | -43.55681 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 182b803c-dbb4-33ac-9b12-c9ddd2a9b0cd | -6.94982 | -42.88762 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d2193810-2e78-38ec-9021-1ec97e132990 | -7.0826 | -43.66105 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df0a9c7d-8c26-3740-92ac-f15e8f9a91be | -7.17406 | -43.5334 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 686d116f-3c71-3034-9860-06f0ff81b6ae | -7.6266 | -43.63783 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README12.md)
