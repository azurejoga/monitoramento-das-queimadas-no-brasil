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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea8b5e67-4ef2-3aa5-828b-229b72e2ef65 | -7.62905 | -55.28991 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e45b31d-f27d-31f5-b99b-0e6f8dc93d38 | -9.45707 | -45.62743 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 88fb3a08-8a38-3abd-babb-95908ca61153 | -9.80327 | -59.43858 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 848ecdac-5f3a-3a66-9625-27406007fd6c | -7.29396 | -56.68154 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10e35cb6-23ba-3f4f-b74b-7cb1b77906c1 | -7.11359 | -42.75407 | 2026-09-01 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 70607782-b9db-304d-a405-692cadefca7a | -6.93339 | -55.63176 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb10ee39-8f64-3891-8436-9a6f5511b670 | -6.37267 | -51.75755 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39cf907e-81d5-310f-9efc-194721b17d3a | -6.75938 | -44.57839 | 2026-09-01 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d340262c-12ae-3666-b366-7492c31d9819 | -11.25617 | -50.57647 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fae45119-4554-36ae-a787-b5b28455cc98 | -6.91798 | -55.70469 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4c490d3-6c94-33a2-b9fb-05ba6c41417a | -7.90372 | -44.25552 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f21dca90-a553-3dca-a59c-1833e85f4211 | -4.94547 | -47.65448 | 2026-09-01 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 93798def-1666-3eb3-b4d0-00a7d05b3a7a | -11.28213 | -50.60573 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71b4a9f2-13ce-3256-9c61-7eac509110cb | -6.5556 | -55.13808 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc16eb5a-13ae-3edb-b456-5521b0c588b6 | -11.66288 | -47.61692 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 147d5fd2-912f-3e8e-b389-0c49220cf64a | -7.53593 | -61.38632 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15842281-b93b-3d0b-b441-305a40d0bf6a | -10.84339 | -54.03815 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ad86b0-e116-35e2-b03b-baa1bcd4e405 | -11.23199 | -45.15859 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ea6103c-ffaf-3683-b399-4ef9064b2340 | -6.96239 | -56.43853 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98731678-923d-3899-a3ff-6ae1b4e2687a | -6.13467 | -53.5332 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 479cf874-f06b-3dc3-884d-0395bce0a69d | -5.9442 | -57.6935 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7eb0e2a-5fd9-3cdc-a055-280fe051d8ca | -11.25286 | -50.57594 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ac61369-7846-3d86-bcac-d1f1de0c268b | -6.37894 | -51.76254 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c781dc17-4798-3619-9171-bcab69b3ccd4 | -7.33707 | -60.59282 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e76decb-40ea-3cd4-bee0-82020f50c4d9 | -10.7883 | -50.50105 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da353356-6790-3608-9080-58b77f11e225 | -6.70165 | -55.41092 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bddd82b1-e0d1-3ec8-a6d1-113ab0891015 | -4.97021 | -55.84423 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ee3926b-996d-3f43-a75b-0838ee779001 | -9.22369 | -47.98684 | 2026-09-01 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 005773e0-5c1a-331b-8ad9-320eacbda8c8 | -9.83798 | -47.8299 | 2026-09-01 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e93cb858-eea7-3a56-a298-44ada7781ae4 | -7.64162 | -46.71273 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aff1c8d-19e1-39f7-b432-b5effce73f7d | -10.97431 | -48.41151 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| face2f43-2353-3395-9c24-df3580e4a2b0 | -8.27614 | -54.92237 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cb279af0-8da1-356d-836c-f078df205784 | -8.93364 | -62.36524 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46168161-a14a-3c2f-9a1c-e7b4329ff3a9 | -11.30923 | -45.19702 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2830ce2-0b99-3385-938e-df47926674b1 | -10.74027 | -54.02649 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40543a29-e5fd-383d-93c2-ddafa0a85d79 | -11.28544 | -50.60625 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23fd062f-c7a5-3694-9723-702dcaa85687 | -11.32022 | -45.17839 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 688100d4-37e4-37f0-91e2-55998b226f5e | -10.35815 | -50.0096 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dd32115d-8c46-327a-a9d7-9c9c1a3f3ad2 | -11.00712 | -48.38124 | 2026-09-01 04:40:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10e5d5a5-4b0b-37f3-943d-297b49fd4217 | -9.16209 | -60.29267 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a062caa4-3328-3133-ac2e-066e18a45033 | -6.51348 | -55.23724 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd8e3be2-8306-3856-9f16-644070eda1af | -11.67369 | -47.61854 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 790c22d0-e79d-38f1-bca7-522334f4ca56 | -6.72683 | -50.46253 | 2026-09-01 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d07112c-6b2f-37ad-8f2b-158aaba77014 | -5.88996 | -52.15819 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 426cd74e-375c-311e-8534-b81cf12e840c | -11.10765 | -51.54052 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d8aa4490-0570-3761-945e-5f6cce12c4ba | -5.24419 | -55.90358 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4adf288e-046d-327c-803d-1f8fc599fe74 | -5.24791 | -55.90866 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4cff84b5-7573-3fc3-b8b8-714976c07afb | -7.3106 | -46.99266 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c6a90dd-a1db-30cc-b54b-44e71df4039e | -7.98153 | -52.08359 | 2026-09-01 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1075e073-5ed2-3296-ad5c-d37c99d796f5 | -10.51288 | -57.43119 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 392302fc-5ad7-3a31-9bb9-46235230d8f3 | -11.24906 | -45.15751 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf31d34-240c-3775-9ba4-0d16285266b9 | -7.17897 | -55.41764 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4772d4d-f4b7-34be-81d3-4e132168a5a8 | -11.19882 | -55.11016 | 2026-09-01 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b646626-40c4-3923-a6aa-b1eb51036e69 | -10.03252 | -44.68553 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed8c5cfe-6ed9-3f65-809a-54eca2576df3 | -6.35047 | -44.09362 | 2026-09-01 04:40:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 963df62c-14ff-3dbf-969c-7f463519689d | -6.24966 | -55.43839 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 368bea60-e057-3123-9477-aa35262d5604 | -10.06309 | -59.40761 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1524cdd-5a95-3b03-b87d-1032b1651706 | -7.53211 | -61.37806 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e11d630-83e4-35d1-a1e0-fcc43b77a053 | -11.25123 | -45.14196 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f0eef89-12d2-37ef-a0ed-0166c5805fbc | -10.75207 | -54.06858 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f96cf84c-2255-3872-8650-f665199ba1ad | -6.80345 | -59.45793 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdd0cec2-8a7c-3cfd-a7c1-15ecc9bb1c17 | -10.67446 | -46.27269 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a1e02e7-793d-358e-84be-398243b8c127 | -5.94969 | -57.69147 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57f1fcbc-15e4-3b23-95da-2bfbc76db749 | -6.29275 | -53.58792 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ffa947-e776-31ee-9301-c264f6d08690 | -6.7854 | -55.63782 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65fdf1cc-32dd-3b31-8145-9f1d5757a477 | -10.40532 | -48.22969 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aec82f9e-6ada-3d82-98cc-44e678407e8d | -6.24651 | -55.48331 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4424b7e-af2c-3e9e-a49e-4eab3eb51a62 | -11.63597 | -49.42519 | 2026-09-01 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13ec95e4-c4f7-378d-9b9c-ec62ee057cdf | -9.67907 | -50.8528 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b9a7f5e-18cb-37a2-b620-ba2ef96a50a2 | -8.77613 | -46.44968 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a294c84b-218a-3b21-81b4-e077fef77468 | -7.35133 | -60.58165 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4595b004-08b0-39d2-b030-8bbc2dabf73b | -10.34544 | -50.004 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 72c9dc86-bb82-380d-83a6-30d669ad50f3 | -5.85419 | -57.55858 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8ae02712-e93e-3cb5-9e03-7009739e9a8a | -9.71277 | -54.33497 | 2026-09-01 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25c689c1-b91d-39a1-a133-e96a84da93c7 | -11.31501 | -45.18562 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 997bcd23-2046-3c95-8927-395ffa68cf1d | -5.95664 | -57.68104 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44f50ba8-53ba-3cce-ac8c-b28ad885acec | -9.79802 | -59.43758 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82b1b19d-e794-3f74-9f8a-110de2720f32 | -7.5304 | -61.38751 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27ba34c1-5406-3c28-87cb-30a9759149dc | -7.03222 | -59.22252 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65a37344-bcaf-3692-9d91-20a73d8a4875 | -8.11572 | -51.6622 | 2026-09-01 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ca0c992-acbd-3fad-a954-26c81bde27e9 | -9.15375 | -59.53237 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05f2f69e-f844-36cd-8c3a-e0a188537d53 | -5.24495 | -55.89916 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71b91b32-701b-3747-99c9-5288e2d809a6 | -4.9598 | -55.8515 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18062ff1-507c-3f0f-8175-bd1f68c25d27 | -11.30195 | -50.58735 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3717b4e-d7ae-351e-856e-7dadfa96d1c3 | -10.33038 | -49.94724 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09b505d5-4451-34f0-8292-e9dc113eb034 | -9.44591 | -51.56708 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1874362-9f97-3755-a571-df02855cefb7 | -8.62298 | -54.84994 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf10abfc-6717-33ab-8108-feaa6b354554 | -12.12321 | -47.27779 | 2026-09-01 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d92a5d0a-006e-3291-97f6-fcc517e60052 | -11.06539 | -51.52957 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a32882bc-d125-39f5-997f-5bca2b68aa01 | -10.35538 | -50.00557 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 570b11c9-a1a7-3383-8de5-373a3c752559 | -9.16085 | -59.54127 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1869d103-bbb2-3974-983e-6987288ea38b | -10.33316 | -49.95126 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d82d1592-f206-343d-8b5e-c2897704f0ff | -11.91123 | -45.05107 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae9d4cf5-17b5-3604-ba00-8e48177b77b7 | -11.01001 | -48.3856 | 2026-09-01 04:40:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bc645bc-003b-3ad0-9b3c-6a9ae4444c87 | -9.88804 | -60.27699 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8694e401-ac42-3d9e-9034-c5a0f6c242b5 | -7.90501 | -44.27642 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32e810c8-cec4-3e10-938e-49702c8926ff | -5.25388 | -55.91134 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40c21f1b-0fd6-3d2c-a24a-a93f8748ab66 | -6.48475 | -43.78684 | 2026-09-01 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da2d0b54-2fc5-3e10-9e4f-53e733340cae | -4.80144 | -55.97293 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 583903e6-6b65-30f9-8b47-c72882be7df7 | -6.0886 | -57.72072 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
