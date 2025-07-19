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
| ac0d60d5-9047-3627-a3dc-b90a5395c235 | -9.60087 | -40.60676 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c860c5be-5bdb-38b3-84b2-b54438619f30 | -7.22983 | -44.13091 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12f656e8-c683-333b-b9b1-228f6d231674 | -9.81153 | -47.73478 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb651d87-61e9-3956-ac13-3962b40d5eb7 | -3.61397 | -43.54454 | 2025-07-19 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93113aa7-03f1-33de-a0ff-0402c4511fba | -9.80651 | -48.56079 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4c87dee1-0f19-3ca3-af03-088bf5134987 | -7.49017 | -43.93519 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d82a608-7835-3653-897d-0a8c9d9395aa | -10.51125 | -42.39974 | 2025-07-19 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| af242134-a57e-32d3-b869-a1fd4ed728ed | -8.26599 | -46.08418 | 2025-07-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e061802-f84c-370f-8888-02e68eeae224 | -2.90437 | -48.24779 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 59c01cd9-4d1b-35b5-a705-255abeef2164 | -4.60519 | -37.88674 | 2025-07-19 04:08:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a33d962c-9aae-3142-a364-91782bfdd661 | -4.64923 | -43.12031 | 2025-07-19 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f636fb2-5dac-393f-a2c4-ed19b79c5db9 | -7.30269 | -46.26117 | 2025-07-19 04:08:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a759e9f-a78d-39f6-a707-d3830b678347 | -6.91155 | -44.83102 | 2025-07-19 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bb0b09d-8826-34ad-9146-ca93a68ee9f1 | -9.81008 | -48.56572 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 22290c18-b3b7-39ee-b8ac-d66abe079311 | -6.87802 | -42.74789 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c070b6f-97a5-3527-b0a4-6a0c9316601b | -7.12846 | -40.12953 | 2025-07-19 04:08:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f355648a-5f7d-3935-ab38-10ef7d6c5587 | -8.04949 | -42.15636 | 2025-07-19 04:08:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 811ecb33-c6f0-3b37-95ef-1ceb3a54c9c4 | -9.80151 | -48.56406 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe52b683-8744-334c-b395-c33be18c1ae2 | -4.66192 | -41.95892 | 2025-07-19 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 46d661a6-1083-3c0e-86e8-17c28990f515 | -9.60345 | -43.85828 | 2025-07-19 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c15e4983-929f-3886-acba-1c9115538f09 | -7.22857 | -44.1386 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc6a2f7-d0cf-3ef9-a447-2e40750b5794 | -3.39112 | -47.48321 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49eb699f-3162-3057-9740-30f7cfc4064e | -6.95251 | -50.46268 | 2025-07-19 04:08:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d2eb382-e4f8-31be-b530-fa64e3bfa907 | -3.11959 | -47.01231 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7e46b252-8ec2-357a-bd65-b57690aee97f | -9.04543 | -40.57197 | 2025-07-19 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c71d491-102f-311d-97f3-6a2340da83ba | -7.19717 | -44.23196 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9327dc80-8f29-3ad7-8bd1-5cec912b7ca9 | -7.72305 | -45.89146 | 2025-07-19 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a0e1dc-169b-3154-a79c-3f5846231d00 | -5.65636 | -43.7172 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 65897dd0-bff9-3fa4-948b-1c29f871b0fa | -3.61108 | -43.54011 | 2025-07-19 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10df63d4-8725-3339-86d6-539c40b734be | -6.51409 | -44.59872 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04b2b249-122d-35ee-a730-6046de827711 | -4.31159 | -48.10779 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| cc0e1f09-7df7-3999-8112-3764efb6d58a | -7.12901 | -43.29157 | 2025-07-19 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24c6c505-b17d-309d-bcd9-b1f54769a834 | -7.09948 | -44.32778 | 2025-07-19 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16dc2c84-eecd-3447-9a5d-71639d8bb6bc | -6.89137 | -42.77155 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 480dfb13-c83e-3397-9122-87fb12f14406 | -7.4889 | -47.49986 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cb837d4a-3e1e-3b90-8a8b-7e4087a7040d | -4.30703 | -48.10703 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| d815b8ca-955d-33fb-8a10-3676288c5d60 | -9.80277 | -47.73695 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00b9e98f-0f13-348f-9938-b4d7fa825ead | -5.64341 | -43.71506 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d13a0a2a-05e6-38b0-b203-a5ebe50f173c | -10.64664 | -44.48841 | 2025-07-19 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4644bf86-15e3-3924-84ab-bd82a9e07019 | -5.64687 | -43.71559 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 7be2e3b1-5ba9-3205-b80d-84b4cab2c1aa | -3.58721 | -47.52598 | 2025-07-19 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ed0053d-f5dd-3576-9bd9-094e0aef931d | -7.2292 | -44.13476 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2855d9f-621a-39c2-aa09-c442602f51d0 | -8.01601 | -43.67865 | 2025-07-19 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a48fc28-cc80-3437-9ba5-ce0703cb427c | -7.24729 | -44.50838 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36131e83-d2d4-3027-9c60-054e9d786776 | -10.65004 | -44.48897 | 2025-07-19 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccdb9cb8-a6d7-3dc4-ae1d-a1ee1adf8b13 | -5.9882 | -44.2609 | 2025-07-19 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31049ae6-d53a-3adb-a241-fe703ebf2961 | -3.58572 | -43.27301 | 2025-07-19 04:08:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 601d5b72-3e66-3209-802c-72f7e69e5a30 | -6.16065 | -48.05043 | 2025-07-19 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| fa51ea93-524b-3135-81b0-ad1160b6069b | -4.60942 | -37.886 | 2025-07-19 04:08:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2d2479be-6fc9-3836-a3b1-a3297404de24 | -5.65663 | -43.72098 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1cd8b4ae-dd9c-30dc-ab06-98c232c5eafb | -7.11215 | -44.38205 | 2025-07-19 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 589d47d5-6d96-3d4a-ae7b-25719e650f5b | -8.25996 | -46.07394 | 2025-07-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33d2fbd5-f00d-3c75-a03d-193f9f43bd07 | -6.16377 | -43.75369 | 2025-07-19 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f150f3a8-e0ea-3b25-8bd4-b23245fb0af8 | -3.04479 | -49.42688 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 950a7b1f-2949-3d04-84c1-1be021abde66 | -7.94721 | -43.95471 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ae647a1-6021-3378-b626-bcfcc2fe11c7 | -2.9091 | -48.24852 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5297c4c8-2a52-3c34-8255-838cbebd90df | -9.60624 | -43.86246 | 2025-07-19 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f2a9279d-9d85-3ed0-9e96-8b58efc23b84 | -9.81371 | -47.74637 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee43b81e-dc0e-3e7d-b616-42ed2ed4ed3f | -7.63222 | -44.30064 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58aeda77-f6e8-3386-b501-e7f320c4d3f8 | -9.48707 | -40.38685 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 46f42d80-a5e4-388f-a5e1-bb0bb7d62c53 | -4.48195 | -46.07502 | 2025-07-19 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0da8cf06-fe86-38e4-a7e7-74256f25277f | -3.11527 | -47.01162 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 855ae37d-a86f-3451-9232-174b3ea0d3c1 | -7.17532 | -44.10229 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7817281-47df-355a-9937-f28769daa9b1 | -10.09098 | -47.2382 | 2025-07-19 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2699fe2b-9d94-3ee6-bb2b-e3d03e846808 | -5.64972 | -43.71992 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| c89796af-c124-3397-a637-a2fa04ff7cdf | -9.60484 | -40.60358 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fae1dd45-dba5-3906-8f8c-124ee13a3b45 | -8.53024 | -47.84384 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d83a20d-038f-36ce-858f-e552938bbbf2 | -6.40952 | -35.33401 | 2025-07-19 04:08:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 011f104e-4df2-3804-b6ea-4974a3a5beb9 | -7.096 | -44.32719 | 2025-07-19 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 548ac772-3a25-35c2-a1ca-ea3dac56d598 | -8.88342 | -50.15934 | 2025-07-19 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 026dd5ff-9ba5-35e2-8a2f-3bf1be50cfaa | -6.28091 | -39.89334 | 2025-07-19 04:08:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f56e8aeb-5c26-3d58-9b4a-7ab64cab3254 | -7.35245 | -45.32067 | 2025-07-19 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f403869-fbf8-33dc-8958-67ddf66320a4 | -9.80963 | -47.74571 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfa93991-010b-37a2-8f18-7464c8606d35 | -6.16946 | -48.05197 | 2025-07-19 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 95330d0c-bffd-36cd-980e-4111ff37f793 | -8.32933 | -47.49751 | 2025-07-19 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a4d3880-cd9a-3be9-80cd-a5d130020fcc | -9.61706 | -49.02267 | 2025-07-19 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37eef8e4-6d9b-3915-80b5-515fa3407c28 | -5.64566 | -43.7232 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cfb1d506-02ce-3af8-ab16-64e35a0ef330 | -8.53378 | -47.84838 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed54207f-ff66-37fe-b46b-48d793f6c3ba | -3.04578 | -49.42088 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54207b2e-5523-3e49-ac0b-aab2a36ad2e8 | -9.83908 | -48.37376 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc3cb846-fe3e-324a-b3d7-eccd4f4ab9ad | -3.92558 | -43.1674 | 2025-07-19 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d61e243-5cea-3ce1-9521-135f41b4162e | -4.87222 | -47.75861 | 2025-07-19 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cdee3ba-4aa9-3ab9-990d-1c1f5f07cfae | -6.6135 | -43.06558 | 2025-07-19 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80cab48e-fd6f-3f73-83ef-838b03443000 | -4.82258 | -47.31717 | 2025-07-19 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33a1ab1b-c070-3e45-ba33-ae0b1991fd56 | -3.12391 | -47.01299 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 86316a37-2690-3b7c-be98-1556dc623367 | -8.01438 | -43.66714 | 2025-07-19 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e965fb8-b3f4-37c1-952a-dea9bd5d34a0 | -8.74247 | -46.67965 | 2025-07-19 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d4a4c78-cc55-3f3c-b024-cd3d081e8421 | -8.0138 | -43.67081 | 2025-07-19 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1be6f009-d3a9-3b79-807d-5ca0621b9c8f | -4.56316 | -48.01169 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccf08ac4-b34e-3632-b9ac-adc72e38a9f1 | -3.5104 | -47.22124 | 2025-07-19 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4fb381d1-584a-3b88-a483-0dfe89e53201 | -6.83803 | -42.7416 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9cd5bfed-22eb-3247-a456-776c194ea017 | -7.3561 | -45.32125 | 2025-07-19 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b1ce178-a5f0-3f19-8a2c-f7b9c9bf272b | -2.90992 | -48.2435 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e7184928-bbe4-3307-b863-6721361e1780 | -7.48826 | -47.50365 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ed9e19c0-7d81-3b37-bda3-9e2c72a98ea8 | -3.36084 | -49.16461 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bea79048-1e1b-3b81-a367-16d89d9fac89 | -2.91546 | -48.2392 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 52283a67-277f-3ac9-826a-38eb457417a1 | -3.58491 | -47.51215 | 2025-07-19 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d31902e-5994-375c-9f12-7614529880c5 | -10.09491 | -47.23884 | 2025-07-19 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21b56384-641d-33bd-b5eb-95ea06aa78ea | -9.81434 | -47.74273 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 148393c1-2c81-3b88-8136-35ae1d75e44f | -6.34516 | -44.04768 | 2025-07-19 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
