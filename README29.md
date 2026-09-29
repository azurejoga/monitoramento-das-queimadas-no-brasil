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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42c6266f-833b-350a-be80-d5cf19fe40ae | -21.06141 | -47.03944 | 2026-09-29 04:17:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ee30fd3-8340-3737-a91d-0312c822bfb5 | -11.36748 | -47.44247 | 2026-09-29 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4fe684c-9a82-3229-9a69-04d5a8c2f471 | -12.75897 | -47.29135 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ed869da9-2e8d-31f3-8e8a-d3b3ee04ecd2 | -20.35524 | -40.97963 | 2026-09-29 04:17:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e376f27a-789d-384d-98e7-9a044b71f3f8 | -16.38157 | -46.90249 | 2026-09-29 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82e4046d-19a2-3031-953d-f3d673ad7a86 | -12.66009 | -46.99363 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc11d796-42ce-33b3-89dd-d7a97a70dfb5 | -12.66292 | -46.99799 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a113607e-a773-3e29-8192-1fc556810097 | -12.61236 | -47.2798 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ff11cae-9464-3ad5-927b-32c65881c343 | -9.80394 | -49.28347 | 2026-09-29 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b10bceed-796d-39bd-aa06-066983e918c9 | -12.00176 | -50.94598 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d0b256e-d1f4-38f6-9eb9-cda714e1c4e2 | -11.67957 | -44.54171 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3def8a93-b70f-329a-a65b-93cf20cfd5c1 | -10.43277 | -49.37609 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 655e7a5f-7691-3680-babb-5c06df246d00 | -14.12219 | -46.28508 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f06161e1-9ac7-3974-8318-186a9c04851e | -14.51114 | -48.30293 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db5248a5-847a-37b0-829f-e84e4340749d | -12.59705 | -47.28538 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b3e424a-7b9a-3267-98f2-0828f87db450 | -16.90885 | -42.10226 | 2026-09-29 04:17:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec32bb8a-7735-394d-8ddf-fba21f81b5a9 | -11.80737 | -49.05428 | 2026-09-29 04:17:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c488efb4-9716-3b05-a7dd-b05dd538eb6e | -12.00274 | -50.99054 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4ed164e-a54e-3b5c-b19b-4df954f3b9b7 | -15.08479 | -48.33078 | 2026-09-29 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5224dd9-2930-3f09-9cca-0ef270f59104 | -11.40697 | -43.44548 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7cdc972-ff04-38e3-9fa2-537859c750ba | -12.01635 | -50.93982 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3be48c04-4b70-3899-a7f1-edbbe4fbc936 | -20.99601 | -47.04346 | 2026-09-29 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b4ea50b-652d-3ebd-af83-deb6a9be1d5a | -11.30604 | -43.5495 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a97d204b-a8d6-3802-be77-738c9549e2c3 | -15.3417 | -48.12307 | 2026-09-29 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b196c18-d9c5-32a9-9c31-d5d903aae21c | -9.77485 | -44.81815 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7b7a2be-163c-381b-a9ba-d13b6b1cd934 | -11.39589 | -43.45105 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f02c5ea0-0107-31e6-ac98-9f7ffb4f3883 | -10.43215 | -49.3797 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e14e59f7-d76b-3745-9470-56bebcd91169 | -11.13755 | -50.03301 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a65dbe61-2ac9-3d96-81bc-4090279dc249 | -12.75549 | -47.29074 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7364553e-08df-3d24-a13b-195ee2ca384f | -12.16502 | -50.81704 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04171eae-148d-34a7-b3cc-1d1a2ce0cf37 | -12.75657 | -50.67325 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31ba575a-2bf6-3246-b7dc-99230ed7e54b | -10.95934 | -43.88136 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38048245-8b6a-3bb4-b17a-e7d4ed7b3544 | -12.70308 | -47.36785 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e485aa67-50d3-3659-a171-280710ce60d0 | -15.08834 | -48.33147 | 2026-09-29 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3042c515-1347-3a7d-9c91-f7bbbca8cef4 | -12.95006 | -46.6429 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| baa60c43-3d4a-3881-9b97-a0cb97299309 | -13.33141 | -43.95258 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4330b86a-2698-3f35-97ad-f64e4fba4f82 | -12.2134 | -38.982 | 2026-09-29 04:17:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 07e3b529-24fe-3b59-b858-617c86400d7f | -12.88194 | -44.79117 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aac76f41-3c0e-3fa0-a932-34c768969a36 | -13.16875 | -48.54168 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b704fce7-1d47-3968-9fe2-5d8897574e72 | -11.43308 | -43.45322 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a16ec307-5c59-39c4-bb13-a3714bc34f02 | -14.12553 | -46.28564 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5272efe7-6ead-3b28-8adf-52a589160c9f | -11.66113 | -43.51784 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93d67ddd-885e-360e-956d-2b8e339a29f1 | -9.9605 | -50.16185 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5446c0ab-28df-3f38-b4aa-d9b44993f3a8 | -12.7394 | -47.27965 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 107c04e5-b728-3fbb-8dca-3fe433c5ecee | -11.37784 | -54.04714 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5057cf1-b9b5-3c19-813c-44bd3ba59193 | -10.91221 | -43.85537 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87ae6c1d-0f14-3f57-8015-0324fb904d44 | -15.09396 | -53.8785 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 059c0827-de78-33ae-9f65-dbaaeea4dea9 | -10.80199 | -48.75002 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b06533c-3938-3326-98c9-df7740f32a95 | -11.37461 | -47.44365 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 313a0f08-8208-3a00-90bb-32bea66dcf1d | -11.37505 | -43.36364 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adfde3f7-5233-3594-b875-96a48eebaa5a | -11.40079 | -43.41893 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a48be36-0c4a-32a6-86e1-7609df7cfb19 | -12.69957 | -47.36724 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f98f7cb-bc92-309b-8da7-03f42382c852 | -11.4298 | -43.47462 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3cee4742-0ecd-3e47-bf2a-90133027b3cd | -11.64891 | -43.5086 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38775758-1cfb-3f9e-9e38-6500fd5f5cc9 | -12.19738 | -37.77224 | 2026-09-29 04:17:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ee8031e9-43c2-36ae-9d9b-8516594c2e44 | -10.13664 | -43.9002 | 2026-09-29 04:17:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17ba21af-e44b-3ecb-ab62-eb0f4f03fe67 | -11.44421 | -43.46957 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a128fb7-5feb-3e78-8088-d425afdf8b4a | -12.02481 | -50.96792 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4f4a3fb6-3eec-327c-924d-689bc6592229 | -11.38932 | -54.04557 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e39ce84a-30a2-3609-b959-8cd43565580b | -12.70561 | -47.33134 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 767e479b-1848-32f3-bff5-853723b7e939 | -15.64639 | -47.73402 | 2026-09-29 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 129b3de2-1c87-3c5d-8f1e-cba8419e5f83 | -12.00478 | -51.00429 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94f2041c-46fa-30c7-a8d6-116862ff0796 | -21.06229 | -48.83746 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 432e8e62-121e-322b-8227-643507d3fe1e | -13.19539 | -48.54126 | 2026-09-29 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b4842bb-c7bd-3b6f-9859-68415e31e57b | -11.61503 | -46.78598 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 336903f0-0e75-3a05-a798-ad3790ed85a8 | -15.49243 | -41.55299 | 2026-09-29 04:17:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d2b6a6b9-279a-33b0-ae7e-1bcba4ca3a3e | -13.08682 | -47.39383 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd1c0fd3-87f5-3c22-ada5-c67732b76574 | -11.87067 | -50.46277 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 782fc8f3-1c82-36e9-9790-6539dbb8749b | -12.22264 | -50.69088 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4205749-6a55-325e-b588-0681d81a2e27 | -13.3299 | -46.81413 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5219f54-44a9-3f03-875e-f1bc6c3b5d1f | -11.41303 | -43.42816 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0787e9f7-7d6e-323a-8e82-fbcaacf1e4ab | -10.81458 | -48.72229 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 429c9f81-8dbe-3441-b720-ca37658c7d0f | -13.38327 | -41.33879 | 2026-09-29 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9e33f26-3139-3aca-ad4c-f56f72b94c43 | -11.38405 | -43.39435 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22e6c8fc-3a89-300a-83e2-9d44849ff514 | -14.07383 | -46.32917 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c588ceb2-4fef-3e64-86d9-0104e5ea242f | -11.41751 | -43.44347 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3433e56a-8bf3-31c7-8af8-9f078ed324bc | -15.17501 | -46.17273 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5336d9dc-01a5-3b7e-b4d2-febeb5e9a4c8 | -11.07169 | -48.89723 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb1f77d5-b74a-39dc-918e-52e12355f2d9 | -14.30356 | -44.99059 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70275573-1a6a-3d16-a0fe-4bc1e6cddf70 | -14.76163 | -45.67016 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e3953df-609b-3f25-ba96-b2270e8e1ecd | -12.76978 | -50.98824 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a1c89e2-48fa-3700-8080-ff4d6de24b5a | -11.82891 | -46.89717 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6eaf625-1778-35b9-ae13-7ae3f8715010 | -11.35417 | -54.05379 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2ef78b9-d161-3c6e-8029-991567f9e734 | -15.20941 | -46.17095 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c4dcc83-4e3b-34e1-8258-dccb13c0b327 | -11.39104 | -47.45495 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdcd3eb2-7d93-3901-adc0-442c2e4725e4 | -22.09755 | -46.96095 | 2026-09-29 04:17:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37102e99-ffec-3511-a8d0-fb32942829ac | -12.05769 | -50.21666 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac3b5e54-d0ca-33ef-a36d-db2bfd9d27ef | -12.68401 | -45.01434 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 064420f9-5770-3a73-a0e7-ef523e388bf4 | -15.18863 | -46.13049 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9b88436-0e0f-307e-806d-5bcda29f66cf | -11.41582 | -43.43225 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4567476-8f7e-371c-9f80-dbaa64cee4fc | -10.96211 | -43.88538 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80d89417-3e0d-302b-9b16-5d82a675ddd7 | -10.78255 | -48.74757 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc751631-e397-34bd-8a92-4fffe7fe451a | -10.01128 | -45.17177 | 2026-09-29 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41cd19da-4bb5-32af-a0d3-52965a02aea7 | -15.15472 | -43.61141 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 625f3ee7-12a1-3d41-8963-9e56c7d1665e | -11.6276 | -46.79594 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050d7b6f-b186-32e8-925b-c4e6a316e17f | -11.44754 | -43.47009 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 271166d4-495a-346a-9857-7bc8360a6754 | -14.48438 | -43.26313 | 2026-09-29 04:17:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3bef977c-1a29-3162-a088-f09f73ac342e | -20.82762 | -57.69188 | 2026-09-29 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 89fac585-df62-3b6e-b494-f0fe831c5f3a | -22.04368 | -47.15309 | 2026-09-29 04:17:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b69c5bb-6698-3a38-a857-e973cc432031 | -13.32648 | -46.81359 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README30.md)
