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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d0a3ad8-21be-3d9a-bb1f-5bfaf5de30b4 | -7.45611 | -59.93291 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a7d7c0aa-c873-3890-b1b6-b5ff98f57656 | -10.85579 | -45.36745 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 943158f7-1fa5-3a67-bd18-c0e85afedbd3 | -12.9598 | -45.92433 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1c6be57f-2c11-395b-b425-03401e065a19 | -5.77513 | -44.134 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c850ea82-e367-3a90-93ce-c2c3d25c851a | -13.57009 | -55.14521 | 2026-08-31 16:50:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9bf88cb0-8b46-3752-b2e1-d9707c415536 | -8.75431 | -46.46317 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1a8906d4-92f5-365f-82e2-870e907c0e57 | -8.80504 | -62.50148 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a94f0c4e-6a4a-3402-804f-e31825f5f62b | -8.80815 | -49.1656 | 2026-08-31 16:50:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 645c735c-99ee-320d-98d3-3ee541eb8f37 | -11.07617 | -51.52466 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| c3457564-2f9a-3ba0-ace1-0b402aba48c4 | -11.61761 | -49.41253 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 5088dc5c-80d5-3d3e-9adf-1016dd01b82c | -11.32279 | -45.18756 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| ebce8942-575b-333e-9d16-0f5e1e8f019b | -10.45748 | -46.54732 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 98edf221-c0f6-3dcd-b860-5496cce72b06 | -7.55598 | -60.46667 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e9b85b44-1a4f-3b0a-9f63-c365856c2de5 | -12.11554 | -45.02821 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| c9124b6f-0861-3623-abde-5d31fc7e005b | -7.6231 | -57.61535 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d05e15b5-855f-3b63-b5f7-70ae0bace941 | -9.39467 | -60.57532 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| de3f9632-6282-3b64-a18e-f21fe32d4704 | -10.77843 | -54.03917 | 2026-08-31 16:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a756bfc3-eb31-37f0-816e-e0782bdc679a | -9.96515 | -46.78221 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b94a5079-1f94-3faf-ba8d-9898e8ccdfcf | -9.87507 | -46.12187 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 790ee1fc-a228-3eb5-a1b1-0280d2ff797d | -8.76282 | -46.45012 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9d937051-de32-3f31-bd2a-256bcceccd61 | -6.87087 | -42.88926 | 2026-08-31 16:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 17c9a9c2-291c-31ce-a241-52da519bc2a3 | -11.05141 | -49.67974 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 877eb34a-5dd1-382f-8a7b-ead9385b88d3 | -10.1253 | -50.32658 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ef7dcb52-ce75-3bb2-91ec-706206dda917 | -8.92843 | -45.02688 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 40760021-6e2d-324d-b5df-3c5248e80402 | -9.21241 | -59.4728 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 573cdf44-c5a1-36a4-aefd-77da09dd0807 | -11.08962 | -51.54046 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 134aa7c3-efd1-3d56-98ba-c4e5c3077450 | -8.04629 | -61.72581 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 338f8f36-3c65-309b-a349-ffb1b2fb97e5 | -11.48775 | -58.52123 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 4e6cc0e1-1939-39a3-b66b-df4b09ed4cde | -8.7378 | -46.46542 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 724c9d1b-d2b1-3d2b-b5de-42c7a2db7944 | -11.21316 | -46.11776 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ebcdd7b1-6df5-3ac8-ab18-e0be2423a562 | -8.35937 | -44.79365 | 2026-08-31 16:50:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2d05da0-957f-3e92-8c50-e9a2a7548bad | -11.93644 | -45.06269 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 537c44a3-09fa-393b-af13-ef0d5967823f | -10.9895 | -48.38361 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 1a4ac00b-9ae0-3b72-b15b-472011fa89c3 | -7.67985 | -44.73873 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f22ad586-41f4-3fb9-bee3-dfe2977fec21 | -7.21637 | -42.77281 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6abbf210-2e16-3836-9387-dfaea6082dcc | -7.05808 | -52.71477 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 51d0ee43-91ad-3228-a856-8c6038cb44db | -12.07012 | -47.19799 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 525c579f-635d-36dc-8ad5-577fa9f1314a | -6.62376 | -53.17871 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b46218cc-839f-33c6-a4aa-e39a796d74f0 | -11.67399 | -47.59972 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 00d51a0a-cf1c-338a-b395-5027a8102b5c | -5.77393 | -44.12683 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bd417661-d3a6-33f3-81f8-98458de66671 | -7.45506 | -59.93923 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 6d66f9e2-fc31-34ba-9d07-555ff5475467 | -7.55411 | -49.68931 | 2026-08-31 16:50:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f59203e4-b853-3c01-a8a3-00cbfe3db83f | -10.09758 | -50.28057 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0e3b4c1e-3697-31e5-b145-f54fc9e7148e | -11.25634 | -45.10989 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 6eddeea1-6e64-3dd2-9803-b7c30b13568f | -10.12887 | -50.30287 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e662ca47-cb75-34d4-9f19-f12f8d820024 | -11.21177 | -45.35067 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 119bc7f5-d33e-314d-9229-21854fa5dcba | -9.40935 | -51.68775 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bc69135b-4ebd-3966-8d54-a8be0ed8fa5f | -8.75564 | -46.46657 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ebf9d829-1ddb-383a-975d-03091ac9374f | -6.8147 | -43.53271 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 98fa2bd4-6bbb-3055-bfca-7355adc011f4 | -7.48168 | -55.2868 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| de0771a6-92d6-36e3-8875-80c4bff4985d | -7.11239 | -42.21563 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ec961e6a-4534-3f92-b6c6-1cf275d5d612 | -6.41031 | -45.42979 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c070057-367d-3c4a-9cbd-3b9c7a6ee229 | -7.9914 | -44.32821 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 7f5824be-2b20-341f-8db9-8eaae27ea530 | -11.37555 | -45.2005 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3316f71-0619-3052-9810-3e8f777fd88d | -9.43306 | -37.83283 | 2026-08-31 16:50:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 090ef7b8-4832-3262-bf65-9b75da3fd144 | -11.93713 | -45.06686 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| bfd73ea8-13a3-336f-8d83-e7e5b3d4dcd9 | -11.23038 | -45.37621 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ade07d1-6ac0-32d4-922f-39a55a869ed0 | -11.2515 | -51.26071 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 35707f66-38f1-399f-b074-0cd7a2b23827 | -10.99827 | -49.69533 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f75528e5-4096-37ef-b050-d0e5b2d5f10b | -6.93089 | -55.64325 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09abd2fc-62df-3759-b2b3-6504dd1919eb | -6.67823 | -52.869 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 37d950e9-ec0b-35f7-8f8f-f2326748a57c | -11.93561 | -45.07972 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0e743768-7626-3321-b0b4-675e37ddf9a5 | -11.20378 | -55.1046 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 605eb95a-cee8-33e8-88f6-fd13d6a54504 | -11.81616 | -46.76474 | 2026-08-31 16:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7870c2a-f804-3b7a-a14c-690daf35cfc4 | -7.93184 | -44.23863 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0ba2903e-f06f-37ad-ac44-9669acfc551d | -7.51647 | -55.27786 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abafb2c6-6b09-3ca0-98e0-898a93f6672f | -10.4027 | -45.08141 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 69151e92-5246-3171-8790-41ea86b85062 | -7.36058 | -45.08725 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e7d4865f-97ce-3c69-8872-46c5f71d0f22 | -9.16869 | -59.37022 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 45f987fd-ce22-3582-a6f6-560d1d562588 | -10.84319 | -45.31143 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fea6ea40-9d18-3b47-9989-44752fd2031a | -7.56279 | -44.33907 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| deef2256-eb83-3495-a091-ff16741004a9 | -11.19913 | -46.11701 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| d4aac347-6815-33b1-8972-57f13efd7b9e | -13.83236 | -54.03322 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 873e25bd-c9b3-3c2d-bb2d-00d67aa24a70 | -7.29253 | -56.69158 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5e508c14-3dd8-3468-9987-1171840749dc | -11.22769 | -45.06821 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a01b365b-5cd1-33a3-a3c7-709339a595d9 | -7.61131 | -55.2839 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b9f80cf7-c4f7-3c31-8387-d8302198b425 | -7.4243 | -44.25455 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5c47c1f6-7112-331d-b47e-394afb88c969 | -9.42494 | -45.683 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| fd8e1cc7-bbe7-3547-9371-48d17602c585 | -9.97998 | -53.93005 | 2026-08-31 16:50:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 3930a2d9-23d6-364e-9ba5-2fbae43c6668 | -11.21296 | -45.11279 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f2809cd-389b-3662-b6c6-fcd2e64a5e18 | -8.14203 | -45.58533 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0d0ff6a-903a-3e5e-9648-2f444eb65457 | -9.19746 | -48.00341 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4226a327-9bd0-3ed2-b4f8-debb7ed393cc | -9.65261 | -46.06661 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| c840ffc1-862d-3392-bab8-37a6a85627ac | -10.15504 | -45.76539 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| abf2eb6f-4655-3323-bc1a-567fe2279ec8 | -11.25336 | -45.09807 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 94e71066-7a45-3a81-b5de-86240e2140c6 | -8.21014 | -54.94319 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c5ed3ff1-aee7-3a65-a68f-053d5af64cce | -7.02978 | -45.8605 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3bb46add-ec9f-385d-89c6-73ec9f8468f6 | -4.91728 | -40.6694 | 2026-08-31 16:50:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| dfaf90df-9670-3d3c-86c1-b6ee3d6fceba | -6.84304 | -41.68331 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 350b37c1-b345-3f20-9341-4ff20741d0bc | -9.18827 | -51.55587 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a9221c9f-1be5-3ba7-b07b-809795e17878 | -11.24671 | -45.14082 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 943f594c-2401-3892-938e-45c58882b388 | -9.30225 | -45.39227 | 2026-08-31 16:50:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 954e70cc-d281-35ca-ae6e-7f44421b5e8e | -10.73915 | -47.98614 | 2026-08-31 16:50:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 02b3425a-c926-33a2-9f1e-10be56332d2c | -13.43071 | -51.69793 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 37e52849-a2b2-3fbd-b576-34a9620de455 | -11.19394 | -40.55698 | 2026-08-31 16:50:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aa34560f-7e6e-3c47-aab9-2379febf29e2 | -11.25278 | -45.11047 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ce1d607b-0f79-354a-b5dc-c49b27f56131 | -10.55768 | -53.088 | 2026-08-31 16:50:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 39047859-10dc-3953-aa7d-666a113ecf23 | -10.85542 | -45.32217 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 51a06a22-5828-3090-9f27-0e554795aa94 | -8.76242 | -45.39066 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 29d80693-36a3-36b2-9660-8dc1bd8e328b | -9.16529 | -59.36781 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |


[Clique aqui para ver as próximas entradas](README152.md)
