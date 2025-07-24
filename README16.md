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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dc192aa-fcc6-3979-9270-d976bc6ec147 | -6.88691 | -45.2504 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5736058f-f736-3e81-a137-1e2aaf7f033a | -4.80688 | -43.21217 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f004ea8e-9005-3125-afbb-2966cb764d55 | -3.05554 | -47.38083 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f1c4de41-99b2-369f-954d-c3a8e913f983 | -4.05585 | -42.52654 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dbd8570c-09fc-3e96-8052-9eaf1dc95e9c | -5.90633 | -43.46214 | 2025-07-24 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecc8c3c7-a90e-3ccb-9e34-b751472766ec | -4.05824 | -42.52033 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d195c01b-d3bc-3b8a-a774-4d4a7ca87734 | -7.27783 | -44.35118 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc71afd-eeb0-3857-b065-0be2eb046307 | -3.22851 | -46.78697 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 10b925f8-386c-3225-ad98-6e9f1dd9309f | -7.62198 | -44.29246 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6742d4fa-5967-3b3c-8951-72e26b542c8c | -3.35874 | -47.16201 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30fb94a5-6c90-3394-919d-0e94470583af | -5.65186 | -42.5818 | 2025-07-24 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 788f4e51-c6b1-3955-bbd3-5998c86829e7 | -7.54758 | -44.48773 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad9d60ea-1c70-38bc-bc4d-03c9cabfe3b5 | -6.49482 | -43.50647 | 2025-07-24 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81ea16a4-bf35-3401-86e7-4d42c381e5bd | -6.54232 | -49.84269 | 2025-07-24 04:40:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8f94782-4b7c-3b7d-9f8d-ed24f30f27af | -4.06154 | -42.51856 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6cdbd36a-75ca-32b2-a3a1-3cc2302da8a3 | -7.46094 | -49.40446 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ffac4e60-8299-3c8e-94ad-7b237e920704 | -4.0589 | -42.51601 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 606990a1-8daf-3594-9f84-5f83f3029af2 | -5.67824 | -43.66613 | 2025-07-24 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e803c57f-f5dd-3934-a8d2-3ed9bb1a6bb8 | -8.03472 | -47.65053 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec95718b-9a76-30de-a884-f2eb41afbbec | -8.52532 | -44.67915 | 2025-07-24 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e9a45e5-c218-3970-a322-ed9691c15380 | -3.17911 | -49.45321 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| db5324f9-8c0c-3fa1-9733-ba1851e44fe3 | -3.6516 | -48.32295 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 124518d3-1008-3606-8072-513fb54fea14 | -8.30076 | -44.96949 | 2025-07-24 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32bba52-e9ac-30c2-ad61-955e7753aec4 | -6.49684 | -43.506 | 2025-07-24 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adfbfdcb-0586-3a15-8171-c2dbccb45f2f | -3.1691 | -49.45164 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 464d5c01-0866-38f0-80d4-905a121108e9 | -3.22793 | -46.79067 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e4a027cf-a5e7-338d-a0b6-c58cf44ee3a6 | -7.28247 | -44.3481 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3466a56d-52d4-3783-8d50-7856276fa0e9 | -3.03425 | -49.42337 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c4e67f-37b5-36a6-9cd9-4a838b866b9b | -4.05773 | -42.5136 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2ecbf2fa-4eec-3119-a836-26861659eea1 | -7.46149 | -49.40098 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 631dd01c-a014-3a2a-be3d-6b9b3b89ba49 | -3.17189 | -49.45565 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 41efae81-4db1-326c-932e-b787d6191819 | -2.49418 | -47.57206 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9071689-add1-3c0c-90bf-e1991dcf2b98 | -3.32194 | -48.71717 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbdc16db-ca90-3211-a038-0b83518c428c | -4.05647 | -42.52224 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec0d33f3-6d61-380b-a47e-b79b92a71f57 | -4.04887 | -42.51227 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2a470431-bebf-36e0-bf0d-cd2fb51ac9da | -4.05204 | -42.52158 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ebac9fc6-13f2-3f94-a719-a18133cc3ae7 | -7.26037 | -43.07946 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| f3d286f9-3325-3f87-8849-d88185738fc9 | -6.88216 | -45.24776 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36fd4364-cd33-3142-a07f-953fe91cd50b | -6.81756 | -43.99717 | 2025-07-24 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9eb1848-ec9d-3862-a864-1bd6c679330c | -4.05381 | -42.5197 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96970c3e-f4b6-3053-a7dc-572ea87238e4 | -6.74126 | -48.08004 | 2025-07-24 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32c5df7a-29a8-32a7-92d8-2f0a70bd5264 | -2.65738 | -47.39957 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c5abfb2-d9ca-3df8-ab89-301a7a8e0741 | -7.30843 | -49.57604 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00e19fd9-542d-3d05-8ae7-dd45266fbd5b | -8.03818 | -47.65106 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 056a29bb-965b-3101-b59b-998de152c509 | -6.6226 | -43.09732 | 2025-07-24 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86812959-c01d-326d-9a69-16b4eade235e | -4.05267 | -42.51727 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7fb56e43-2b89-3c70-aed0-873b080032cc | -3.0337 | -49.42686 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33ed8940-7495-399c-a451-86c4e765142f | -2.41984 | -51.10535 | 2025-07-24 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b908c9f9-755f-37f1-a4ad-c1ff4d3a7924 | -7.55114 | -44.49198 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 003be516-fd5d-31a7-951d-544da3397241 | -4.78235 | -45.33719 | 2025-07-24 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7fab2954-02c8-3e4a-967f-7d81597731c1 | -4.30471 | -48.10414 | 2025-07-24 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 69167e63-f6b9-32b8-bc18-fea41ee1893f | -4.0443 | -42.52262 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3070f737-7b35-33d1-bbbe-ae59c40ea21e | -2.61785 | -46.85282 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1ed7b9c-9f7c-3171-9fa4-c0c0644e4d4e | -7.15919 | -45.23968 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d938e4e9-5dad-3b4b-ba93-3ff4411252d2 | -7.2559 | -43.0788 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 025ea250-92fb-3a3b-9b49-76e5987c9b03 | -7.48322 | -44.69969 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54fe0907-7fc8-3414-b767-ae20b148bf4c | -6.6467 | -43.05646 | 2025-07-24 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b30c2feb-05f1-3c86-846b-86bb818fc52e | -5.48768 | -42.14914 | 2025-07-24 04:40:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1aa68824-27e7-3d13-b736-385c56720c1f | -4.0495 | -42.50794 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 21a03fa0-fa19-3a06-8c55-d76dc8a149e9 | -13.70427 | -45.66798 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15db59b3-b705-3b7a-bd23-e6346ff2fdbf | -12.42351 | -45.38343 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2e62aa5-b41c-3360-b13d-f037e4fc779a | -13.7089 | -45.6648 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 818383e4-ccce-3ba3-8a82-3b88cacb24c2 | -11.13117 | -48.6389 | 2025-07-24 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27fd1d62-126e-32cf-a706-2e466987e255 | -13.68447 | -47.73848 | 2025-07-24 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f22fb46f-4da7-35f1-94a0-afacb1becf06 | -13.70228 | -45.68307 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 176febd8-b480-33a6-b941-ed13c6d6b27f | -13.70013 | -45.6838 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3bf8ce8-5cf1-3ed1-933c-1ac354974f95 | -12.42456 | -45.37587 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f641157-68f1-3745-b59d-31c858b041bb | -8.58253 | -47.97488 | 2025-07-24 04:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be1e2da6-59cc-36f0-be14-184bc2a2b7de | -10.06565 | -46.85679 | 2025-07-24 04:42:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3c92c8e-1ddd-33d5-8982-57598c8b7258 | -13.70223 | -45.66874 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e554ac80-db6c-3f46-a9f7-65ebaa028efb | -13.09509 | -52.14996 | 2025-07-24 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1844f196-6a47-3e78-9a78-2825c82d9a0d | -7.46134 | -57.66747 | 2025-07-24 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e198347e-66c3-3852-83e5-d261958ee8b7 | -13.69758 | -45.67191 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eece0c4c-4641-39a9-9819-a767fea4fd18 | -11.77454 | -47.40012 | 2025-07-24 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 91f2ac15-58d2-3d36-8127-f7d397223f9b | -10.66444 | -47.78334 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c53e5a5-dbdb-3fcf-a93a-54a6de8cdee0 | -10.95791 | -48.22507 | 2025-07-24 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c777c22-2012-32fc-bb78-0f61f43c6ac2 | -7.25762 | -60.18457 | 2025-07-24 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d64c9ce9-28ed-3541-bfe5-4cf416368402 | -13.71052 | -45.68428 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8cbed71-9e76-3f99-8ea6-252f4ced33a2 | -8.09405 | -50.08607 | 2025-07-24 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d3f6461-9d5d-3af8-8616-98464af867b2 | -8.92697 | -47.34475 | 2025-07-24 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20d8184d-a04b-3312-8a58-6e34928832f0 | -14.17897 | -45.35601 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0efa73ba-f9f3-33b5-9fe0-582bf58ee27c | -14.48309 | -46.35898 | 2025-07-24 04:42:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09633daf-722e-3072-8e08-da31d98bb752 | -12.41991 | -45.37905 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9df01550-0ee2-3033-9ee9-cbaf6140c64d | -10.04469 | -59.10107 | 2025-07-24 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cb303ab-320c-30a6-a3b3-b99352431546 | -10.12372 | -57.76709 | 2025-07-24 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29daea9c-4d6f-3a66-8c17-b6c6fd996d70 | -14.21215 | -43.95632 | 2025-07-24 04:42:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc468fa3-1c7d-3941-9f23-e2ce5fa96580 | -11.94235 | -58.76945 | 2025-07-24 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a638ba-68c3-32e0-ba83-5340d55123e4 | -11.13173 | -48.63515 | 2025-07-24 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9964fe0-9305-3fde-87be-00150f1dba12 | -13.09569 | -52.14632 | 2025-07-24 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b92f6c8-6dec-3e5d-8fde-cdfb96b19ffd | -13.70129 | -45.6906 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f98cd36-7b46-354c-ad79-2bc717cf1e84 | -10.66737 | -47.78782 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 697eb016-ba84-323c-9b47-6605236699d0 | -9.66313 | -48.52455 | 2025-07-24 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b02efa4-f7dd-392a-b870-4e6b7b0ce775 | -12.50846 | -57.7769 | 2025-07-24 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 778f20df-4bf5-3824-8c0f-eb097bebad51 | -8.4761 | -49.55507 | 2025-07-24 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea99dd95-eb90-3f8c-a416-9be700bfef07 | -11.87593 | -55.45013 | 2025-07-24 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb53e50e-5ee6-3be1-b881-8cc4876614f7 | -8.4901 | -47.23345 | 2025-07-24 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48460c36-b0b4-379b-ad7c-6002879ac020 | -10.71056 | -48.86016 | 2025-07-24 04:42:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dc39441-f012-3900-8d92-d1fc820fe29a | -12.25327 | -44.77823 | 2025-07-24 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af020d54-f60d-38e2-816c-7e3f8b05e103 | -8.58195 | -47.97864 | 2025-07-24 04:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0db05a03-99e8-3e26-bb49-9f36cdf10983 | -14.78941 | -42.44356 | 2025-07-24 04:42:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
