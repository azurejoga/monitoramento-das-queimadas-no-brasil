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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 422a8010-3d34-3151-9355-4a1917f5d1e6 | -4.5694 | -44.0657 | 2026-08-28 22:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a4bfc635-1ba2-3cac-a7f1-ea097cbb9bab | -9.1654 | -43.2768 | 2026-08-28 22:30:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 268.2 |
| 21029ecb-88ab-3c44-afbf-bfe7bafa6aa0 | -4.282 | -48.2007 | 2026-08-28 22:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7c495af5-bb8d-3d21-9443-57d3f408fcc5 | -11.7167 | -54.5244 | 2026-08-28 22:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 59be04d2-e663-3bfd-adde-64a8819a3362 | -6.7526 | -55.4861 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c4ca9bee-1216-3391-96ec-88eca5626dfa | -15.6843 | -42.452 | 2026-08-28 22:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 54cde630-a85d-370a-a4cb-3238fc4959e7 | -7.5324 | -55.284 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5a192f9f-ca86-30c5-ba74-3c109c54cebb | -8.9929 | -50.785 | 2026-08-28 22:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 23768fec-0137-39fb-a232-07de20d4b2fa | -11.0445 | -57.2023 | 2026-08-28 22:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 197cbc05-6421-3312-be12-c9f4b18d72d5 | -5.5964 | -44.1822 | 2026-08-28 22:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d8055e89-27d1-3702-a413-2d7dc183b47c | -4.5695 | -44.0427 | 2026-08-28 22:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2a066d92-e3a2-3e89-9527-83577f1fd51d | -6.1656 | -57.7988 | 2026-08-28 22:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| fb4bf5ea-b2a8-35c1-be9a-708b801e9f67 | -4.8211 | -42.8887 | 2026-08-28 22:30:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 91daa104-169f-3978-b28d-0229351f3169 | -8.5359 | -55.3428 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0daeea5d-86c2-3a6f-8680-c7224d2b5267 | -3.7386 | -53.3618 | 2026-08-28 22:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 79ec283c-484c-3412-a6b0-d2a80a2cf241 | -6.6317 | -43.73 | 2026-08-28 22:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d7837871-df73-3ff0-a21e-6e5036d54136 | -7.5137 | -55.3051 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 682.0 |
| 22422d13-604a-3543-8763-7ab7cf09fe15 | -17.5992 | -51.6247 | 2026-08-28 22:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6a32a9e5-8dab-3b01-bb42-807815d58cbd | -11.1916 | -51.2708 | 2026-08-28 22:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4d1c56c4-0fcd-3086-a3fe-f0741de0cf27 | -14.9166 | -47.7376 | 2026-08-28 22:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| b1c97c04-9b2d-32f0-98c7-0955cbf4552b | -5.8894 | -57.7708 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 264.9 |
| de1d8213-c478-3bff-bbae-02951990f28f | -6.7156 | -55.4879 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| ec879f46-8406-3bdf-b9f7-b2975aa4217f | -6.7699 | -55.6644 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 416.1 |
| 874390da-dc55-329c-bf92-c48c77e58d3b | -20.9207 | -57.5723 | 2026-08-28 22:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 6318f37e-3d3b-33c4-b97e-d48e99bd0b04 | -11.7167 | -54.5244 | 2026-08-28 22:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f3373fc0-1448-38ea-971d-ab5babfe1010 | -6.7341 | -55.487 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 215.6 |
| b8c7601e-8f06-3a34-9bdb-e663d249d45e | -5.9079 | -57.7506 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| d73a5dc0-f179-3071-b4fc-994140306ff5 | -11.7165 | -54.5449 | 2026-08-28 22:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6fc19c39-c276-3ba2-9345-4a2e32c96eb7 | -8.5969 | -54.7755 | 2026-08-28 22:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 64ed08fd-2cab-3cd3-9997-0136ee39267b | -8.9741 | -50.7866 | 2026-08-28 22:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 02f98433-b734-394e-ab64-259b6dcef077 | -6.6396 | -53.1934 | 2026-08-28 22:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d1fede07-3f32-3008-ac73-8aa9b718e8c9 | -6.7343 | -55.4671 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 322.1 |
| 70566372-8a0a-3fa0-ae38-571cd1acca8f | -3.7571 | -53.341 | 2026-08-28 22:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 7c145ca9-c609-3fe4-9e55-b89184ebd9dd | -6.1657 | -57.7793 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5509351b-d878-3222-a112-c9b6c4edee14 | -6.77 | -55.6445 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7f7403c9-83ae-3ec5-ac32-61ca890ae7a4 | -7.5478 | -61.3056 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 594f258c-2397-3264-94f3-c25365a66a46 | -7.2847 | -45.8652 | 2026-08-28 22:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 941added-6fb5-39ff-84f1-e487db4e66b9 | -23.1937 | -46.9911 | 2026-08-28 22:40:00 | GOES-19 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 2c56b21b-fce9-3f3c-b46a-18b7c73ba619 | -11.1913 | -51.292 | 2026-08-28 22:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 83a273d2-b5be-3766-8be8-fa6312a749b2 | -7.5139 | -55.2851 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 401.4 |
| c2cfcaf8-3a04-33ee-80b4-678c2513c977 | -7.529 | -61.3635 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e0c49ab1-c73c-38fb-80b7-4c7fea016e4d | -12.43 | -43.4182 | 2026-08-28 22:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 88ea5fb2-2ede-3184-af75-bd92868bf878 | -6.7157 | -55.468 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 7fc75438-be3b-349b-9404-d4192789a232 | -14.9386 | -56.3216 | 2026-08-28 22:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d1eaea3d-8a3d-3057-9dff-3c345a930719 | -7.6213 | -61.3599 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 97c860f1-fcf7-33fe-a766-c1391e94ebfe | -6.3465 | -44.1013 | 2026-08-28 22:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| bdb4f34a-5b30-3ad1-9d92-2b71a564041b | -9.1654 | -43.2768 | 2026-08-28 22:40:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 298d605a-c206-3652-8206-2312b6a78605 | -7.4952 | -55.3062 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 275.9 |
| 0a758540-9435-3ce7-b961-d1256810986a | -9.9708 | -53.9419 | 2026-08-28 22:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 70d8486c-c642-3843-942b-9dbc336db231 | -17.6191 | -51.6214 | 2026-08-28 22:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a552e82c-2152-38c1-97c7-cb256b5b7d48 | -3.757 | -53.3612 | 2026-08-28 22:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 587a607f-721f-3e57-bebe-976f109e6fbd | -18.995 | -47.4332 | 2026-08-28 22:40:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| a695fdae-44dc-3e67-8845-4382f59118eb | -9.9288 | -60.4277 | 2026-08-28 22:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 0f675f35-ee0b-33b9-a317-58aacc260fbe | -6.1656 | -57.7988 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2f502381-1adb-3487-8a28-3e3b4fe55d05 | -10.7596 | -54.0384 | 2026-08-28 22:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 8941b786-898b-3ad5-ac2e-5b71c692aaaf | -5.9078 | -57.77 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| aaf9396b-7bf4-3e25-9fb6-7137010c072c | -5.8895 | -57.7513 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 321.7 |
| 410c5028-9d07-34d7-ba90-d4c98c9705f2 | -8.9739 | -50.8078 | 2026-08-28 22:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| cb617f06-9770-319f-b0c2-ac20462a2031 | -6.6129 | -43.7317 | 2026-08-28 22:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7d8d21bf-4544-35c2-ab88-d3fcf8a1fa0d | -4.282 | -48.2007 | 2026-08-28 22:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 11a428e9-a8dc-361d-b438-351814e978c5 | -8.9926 | -50.8061 | 2026-08-28 22:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| a818d54c-a4b3-39d6-8400-427dc6b11b06 | -5.871 | -57.7715 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a194747e-1f30-337a-b904-15c74c0516fb | -6.6315 | -43.7533 | 2026-08-28 22:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2a6ad376-24a0-3c88-bdd8-4a5ebed6482e | -6.6127 | -43.7549 | 2026-08-28 22:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| aad93f25-30d6-33cb-bf7f-b673f8ee6f3a | -8.5358 | -55.3629 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| af17a022-e8ca-3dfc-9f17-cdb369de05cd | -5.9819 | -57.6892 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 44cff054-1fe2-3142-a23e-49804ce74fe1 | -8.9929 | -50.785 | 2026-08-28 22:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 1c2f323b-f56d-321f-9de6-e9b06f5726bf | -7.5661 | -61.3239 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| baf2d97c-a5be-3c50-a6ea-ccc11ac69e58 | -6.7528 | -55.4661 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| d750ff37-67c8-314e-86b5-5ba30420b82d | -7.5662 | -61.3049 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 80414ea6-eec6-301a-a45a-30abb4705f1c | -9.9102 | -60.4287 | 2026-08-28 22:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0af40400-3bc5-32ec-ab2d-3563033b134b | -6.3467 | -44.0782 | 2026-08-28 22:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f9b397d2-8fdf-3f46-a351-4e2226137a2c | -6.0004 | -57.6884 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e62ac1af-2fdd-30d4-9e62-c86ad68e2cbc | -14.2027 | -52.8432 | 2026-08-28 22:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e3071ef5-a2c0-335b-885e-89cb053e9ce3 | -7.5137 | -55.3051 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 522.3 |
| 402d4e61-4d92-3121-84cc-147f99e3a8e8 | -12.4305 | -43.3944 | 2026-08-28 22:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1046dc7f-0481-30c4-bc25-48a6d7d234f4 | -14.897 | -47.7409 | 2026-08-28 22:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a966625c-4c4a-3941-95cf-8968976f79dd | -8.5359 | -55.3428 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9ba0f403-cde7-37a0-9dfd-1a966c212fc2 | -7.2849 | -45.8427 | 2026-08-28 22:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| cdd0dc1f-a2cc-358a-9f54-c5cd935bcadf | -6.6397 | -53.173 | 2026-08-28 22:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d3c7e84c-1886-3b74-b5f1-b152eb4d2203 | -7.6212 | -61.3789 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| ceef3683-52c5-35c1-8ddf-21f4594067cd | -6.7513 | -55.6853 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| fed9027b-1d5f-3fd1-9faa-a50213b1d9fb | -5.8711 | -57.752 | 2026-08-28 22:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 34505236-30cd-34c2-9d45-c2ccb97f400e | -9.9474 | -60.446 | 2026-08-28 22:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cc1535a3-af9d-369c-b608-4c93191b560c | -6.7698 | -55.6844 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 246.4 |
| 272ed438-5130-373c-a890-f099f617e58a | -9.2644 | -45.6444 | 2026-08-28 22:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9d52502c-e8b0-310f-89fb-731add175c94 | -4.2821 | -48.1791 | 2026-08-28 22:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c97295d7-10e5-3078-b454-cbe19d389724 | -11.269 | -54.0334 | 2026-08-28 22:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4ea644d6-8b20-3d01-8cf1-e0ada476d5b9 | -19.0152 | -47.4288 | 2026-08-28 22:40:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 046cc913-8157-3e50-ba56-39d618b0bf9d | -14.9193 | -56.3237 | 2026-08-28 22:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a7720038-7019-36f9-8d22-3eebace61d99 | -6.7526 | -55.4861 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0fef2ceb-10dd-3746-9528-1114d1d235bd | -6.6317 | -43.73 | 2026-08-28 22:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b27b3415-50e0-3d9b-9ada-ce6887a54939 | -7.6029 | -61.3606 | 2026-08-28 22:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7d39a216-65d0-348d-bb34-062bde70a837 | -9.9475 | -60.4267 | 2026-08-28 22:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ddfbf015-d951-3ce6-9b32-dea9f12f6943 | -9.8739 | -60.2955 | 2026-08-28 22:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ff4d99ea-dcc7-31d8-8edc-ab69164fda94 | -7.4953 | -55.2862 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 300.5 |
| 242f6c8a-2dfc-332a-81b6-e02527bef0ff | -9.1464 | -43.2792 | 2026-08-28 22:40:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| 72991d08-060d-38a9-bd74-5f411d346004 | -7.5136 | -55.3251 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 0961d9c9-8681-3fca-9797-aefd4d892dc1 | -6.7514 | -55.6654 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 3742af68-29f1-376f-bd59-e07223ef6cce | -6.7884 | -55.6635 | 2026-08-28 22:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README192.md)
