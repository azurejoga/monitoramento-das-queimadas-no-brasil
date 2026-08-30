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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 129b1878-5429-3cc6-9f0d-0b2b5572b80f | -11.35443 | -45.15902 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ae14efc-1635-393c-8eca-14de892bfddc | -12.37017 | -48.19252 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 900228f7-3f5f-3c32-a5ee-3f87ced5cc5f | -11.23989 | -54.00274 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0389e2a2-bae4-39eb-81fd-2612189174ea | -8.60704 | -54.77517 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 367d6870-4568-37e2-96e5-822ed138a4b4 | -10.75831 | -44.86742 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5aea5462-081e-3101-8528-460d41f09439 | -11.24222 | -53.98978 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f6ad9cb-8d99-335a-9664-bf87fb1996a3 | -11.65585 | -46.75242 | 2026-08-30 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91115d84-3a01-382d-895a-86cecae1ae26 | -10.75445 | -50.87468 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 952a8401-a553-3a02-bd68-e5e0e1bbf6b8 | -14.25032 | -54.6802 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d926bf9-ec3b-3d08-915c-b281e9676834 | -11.34859 | -45.15029 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0d9fe4d-4e9a-332a-8382-5de5012e517d | -7.24113 | -60.63495 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5432fcc7-6d42-39d1-baa0-cd93754fb363 | -12.77595 | -46.45707 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5031e976-3ffb-3de3-a152-22aa63b2fbda | -11.71544 | -54.5299 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6d65acf-a7a6-3cbd-80ff-c7593ccdbad3 | -12.92089 | -45.866 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c4d938d-dee4-3e82-ad92-c7531441b87f | -14.43036 | -52.55719 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f586fca9-0490-3f48-af18-2a09e463a465 | -10.73526 | -54.03738 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d3cfba4c-ae36-33ea-8018-480c287413b0 | -14.42429 | -56.26284 | 2026-08-30 04:34:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1cc3f494-eb3e-3514-a4eb-c1c22e289c6d | -10.78662 | -45.33335 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef20d24d-4859-3374-923a-35e36a9616e3 | -13.85472 | -54.11364 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d94134d-9667-3ee2-aded-728419fad8bd | -7.32321 | -60.60928 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3dea372-3c52-3b12-b79f-a3252e4953b3 | -11.02563 | -57.246 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44514856-8e15-39d1-b601-ce27de12f74f | -12.68703 | -47.45557 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0acea369-df3c-3bc4-b2d8-0252be2899a3 | -11.80979 | -51.04325 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4f3aff93-d5c9-38a9-834f-f57ab81a5ee8 | -9.17486 | -59.63373 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f64f2e-aae3-3cd4-8d6e-dfcc0e83b9ac | -8.49795 | -55.29671 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e3861fd-33a8-308f-91a7-2fc2ac03537b | -12.77479 | -46.44188 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c18d0c82-9acb-3efb-9754-314c4c357f4d | -11.16377 | -51.31347 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a65d460-e66f-363e-bf12-52cf663a2314 | -8.96975 | -50.80614 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 907d141d-5688-3929-87b5-8805dfa721cf | -12.92147 | -45.86217 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d02ae76-155e-3aa0-ae24-9ecc6b53e543 | -14.67398 | -48.0555 | 2026-08-30 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e3a09dc-bfcf-34e6-815b-59908e142473 | -9.15754 | -59.51778 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f86cff52-1dce-3be3-94fd-c93121852a13 | -11.24014 | -45.09515 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aba6bdc-dc60-34f4-b41d-915b45a08ba3 | -10.75473 | -50.87341 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db427ac2-9e2c-34d5-8485-fc58b809af18 | -11.00249 | -49.6845 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae102aab-2862-3b0f-85cd-e84783e3b928 | -9.42871 | -51.5718 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbce43fd-ee8c-3ce8-ace7-3ae7b39057a1 | -15.22115 | -57.66253 | 2026-08-30 04:34:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d18f627-37ad-38d7-a00f-88884fbd3423 | -16.2029 | -47.75885 | 2026-08-30 04:34:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc76fdf0-8b24-3da5-9ec7-e76b84dd4805 | -11.21395 | -45.0791 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8061795f-db18-3f35-988b-5719ab3658ff | -14.41983 | -52.55019 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 54a01eb4-b68e-39e2-b003-8224c170ee16 | -14.1513 | -52.8134 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72523422-9ec7-3123-802c-a869de33c835 | -14.98827 | -48.1734 | 2026-08-30 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2732863-fd29-397a-bf8d-a47993bd38f3 | -11.21222 | -45.06681 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc2efe17-71e9-317d-ad6a-1317f53f7aad | -10.48026 | -59.61914 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e7a3396-513c-32c8-9e0e-2107e630ebbb | -11.29236 | -54.03816 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 747d6f8c-a1cd-3362-8752-9ce640183478 | -10.75169 | -50.68962 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 834e4dc9-9901-3264-810d-45a590bd3dad | -11.65863 | -46.75653 | 2026-08-30 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fa7643b-02ca-3a9d-8607-3df7d295a23e | -11.53359 | -45.55367 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2c951e8-7ba1-395a-b9b9-decf0bbc2eaa | -10.99701 | -50.5233 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a48bd01f-ba24-353e-b4c2-efbc1ac439c8 | -10.75139 | -53.99931 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55f4d6a8-c532-3765-8a9b-fc6688753733 | -11.18842 | -55.09845 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87426c20-5ac7-3ee9-8610-69f5bca7c9d7 | -11.60975 | -46.72359 | 2026-08-30 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a70beae-2963-3e61-a3be-dab3aef40312 | -14.15518 | -52.81409 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a73427e3-39e2-33a2-a928-c053ae410628 | -11.48099 | -45.06085 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30368d02-2be9-35cc-afac-e3317c00bc6c | -9.15213 | -59.51101 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53c18556-f583-3742-a269-9db935acbcb8 | -10.74817 | -54.02354 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2df6ae0-7297-3957-991a-cd00a06e8917 | -10.47616 | -59.60654 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 626f2a97-b859-3ea1-8694-7e26cc8097f9 | -11.34103 | -45.15311 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c576b97f-84cb-3bc7-9c54-62a5d2bb66b8 | -9.31416 | -47.62873 | 2026-08-30 04:34:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ffb8b7a-6d80-3564-ba13-f6fb1854143b | -11.23672 | -45.1022 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f3a0a78-79f3-346f-99c1-8bc0f6408077 | -11.37098 | -45.42779 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 78dfe12f-f09f-3316-b903-bd6f37931b91 | -9.14781 | -61.0972 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36faff6d-7579-3341-a4a7-a86d390b97ef | -14.93752 | -56.34071 | 2026-08-30 04:34:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 522fdd04-45a4-3fef-ae48-122ec1848bc9 | -10.76651 | -44.86057 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb9ecc04-48ce-3c79-b504-252c1845d763 | -16.14202 | -43.04712 | 2026-08-30 04:34:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae92b311-2420-3d44-9b31-769bbc85ecc3 | -14.27958 | -57.04092 | 2026-08-30 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59e5b936-069c-352d-b8b2-7b531f08027e | -11.29223 | -54.03947 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 39b36a49-de8f-30ca-8cda-3bd68752d1e5 | -13.19609 | -44.06965 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c5063e3-1c06-3a05-96e9-6ac2b1df9116 | -9.93921 | -60.53052 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80b2e053-68e1-3943-9472-4b3a48f274b9 | -12.39525 | -46.42472 | 2026-08-30 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27c861b1-63ff-3382-9603-969d4c73aad2 | -15.12184 | -53.58493 | 2026-08-30 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cb98860-3e3d-3a50-97e0-41e8ef05d502 | -16.86975 | -43.58207 | 2026-08-30 04:34:00 | NOAA-20 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce4a0ef-56dc-3bec-b7dd-0493f2b43afd | -10.75772 | -44.87137 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 763a31d5-a4c7-3f99-8ebd-982cb332cd41 | -9.93311 | -47.60301 | 2026-08-30 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc8f69cd-8836-366a-922a-94e7d1ab51cf | -9.15966 | -59.50675 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd5fbc97-ae89-3691-b46c-7579ad6419cb | -12.08936 | -47.19667 | 2026-08-30 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6036c69-5bd7-3132-9bf2-c7520ca9e4c4 | -14.41814 | -52.55973 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5a16772-fccf-3ebd-903e-68b06855b9a1 | -11.18657 | -55.10869 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce5af0ce-8bfb-3751-b2ad-9efe96238306 | -14.7728 | -48.73992 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f5443ff-6ed6-370c-88c4-36a34d6119cc | -8.49741 | -55.29966 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfa88a65-7a5d-3e12-947a-20281715c6f7 | -15.13775 | -50.63338 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| a05d9bc9-fae0-3c75-87fc-7b01e001f89d | -12.78326 | -46.45448 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a82e3a8-5dde-3f71-8873-3d8ff5acebeb | -19.09442 | -46.23895 | 2026-08-30 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0689b94-f9a4-3cdd-85b9-8265cab56b5c | -21.19308 | -46.8195 | 2026-08-30 04:36:00 | NOAA-20 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7435bbef-b2d3-3633-9e35-a994a30adaf7 | -19.0825 | -57.39686 | 2026-08-30 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 477acdd4-d461-3356-8449-749ba982b550 | -18.10797 | -42.87336 | 2026-08-30 04:36:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ad6e3b88-d1c6-3449-a5f6-b4b78249ff33 | -15.61663 | -56.40738 | 2026-08-30 04:36:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38b994f1-455d-32ee-a143-1f5776a8c3be | -23.15307 | -48.66837 | 2026-08-30 04:36:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a96b932a-5fdf-3d17-81ae-58517f2d21ad | -19.87308 | -44.61397 | 2026-08-30 04:36:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3688cf5a-1de1-3451-80ab-b91105d566c2 | -21.17397 | -50.47263 | 2026-08-30 04:36:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3c931efb-951a-3a9c-9434-a33a7ae145ae | -20.51151 | -49.05198 | 2026-08-30 04:36:00 | NOAA-20 | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed907bfd-9858-3bca-90f4-fa4dfbc3a282 | -18.66171 | -46.84827 | 2026-08-30 04:36:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2108977-564c-3572-a950-cdf8b21df0df | -20.11092 | -48.27453 | 2026-08-30 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e2bf960-a39d-314c-bb59-0ecc3cbf846c | -21.0163 | -46.42513 | 2026-08-30 04:36:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7c38e32d-5f95-3ef3-b0a7-bb4cca98e212 | -18.81942 | -47.45822 | 2026-08-30 04:36:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 272efec9-05d3-3340-a537-a33fe9d1d7bc | -19.47432 | -57.56643 | 2026-08-30 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a7a46ddc-2e94-32dd-a047-ef8cccf78c10 | -23.0338 | -46.59196 | 2026-08-30 04:36:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 203dcdf3-ade4-3c07-9f06-bcbeebfec4d5 | -21.01225 | -57.83381 | 2026-08-30 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d0e2f56a-8228-3a24-a876-80693b0d9848 | -15.64718 | -56.40268 | 2026-08-30 04:36:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa09d063-400c-34d3-ba18-7283099df86b | -19.00782 | -47.32017 | 2026-08-30 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99bb47bb-c1a5-332f-9701-2dbe65810817 | -22.65199 | -47.67141 | 2026-08-30 04:36:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
