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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4ab4bab-562a-3fcd-9746-9c8371bbc5cb | -13.1267 | -57.1293 | 2025-08-16 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 29154708-4b46-38cc-906b-aa4c81c2e3c4 | -12.6139 | -46.9273 | 2025-08-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| ac060959-6544-3881-b90c-b1cf21cb7a05 | -12.6143 | -46.9047 | 2025-08-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 1825146c-7333-3e5a-901b-84929919c514 | -6.5641 | -43.0122 | 2025-08-16 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 6668d245-57b6-34c3-be8e-856e747f3f48 | -12.5947 | -46.9301 | 2025-08-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 73986589-e267-3a84-908c-f0113b2b2bad | -7.9625 | -63.203 | 2025-08-16 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a1facdd4-6d1f-3051-bec6-a12270fedba5 | -11.3657 | -55.4107 | 2025-08-16 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| be206330-c3aa-3e01-be5f-99b392df73eb | -6.545 | -43.0373 | 2025-08-16 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 25e98b9e-2016-36cd-b9ad-abcf15491ddb | -15.1796 | -51.1555 | 2025-08-16 13:50:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7a4a2366-0f62-3149-bcd5-78a1ae73d974 | -6.5638 | -43.0357 | 2025-08-16 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 81cd768d-ae5a-30ab-b72b-9e05e53f6587 | -14.9822 | -54.7328 | 2025-08-16 13:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4c019506-cbfa-30bd-830b-f2fa9a4d9a7e | -11.6614 | -46.6562 | 2025-08-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d4299eca-7c07-39f5-99cb-ea87aae64bb1 | -15.199 | -51.1527 | 2025-08-16 13:50:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 7098aaad-188d-3cd9-a484-c8cafe00353e | -13.8748 | -45.5411 | 2025-08-16 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a57ccde4-309c-31c8-b00c-bfb6553b8d53 | -7.9439 | -63.2225 | 2025-08-16 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 232.8 |
| 4c293d5f-8527-300b-b894-782b5a6a2673 | -7.9623 | -63.2407 | 2025-08-16 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| eed27069-3753-3eb9-acae-2873cd5e7043 | -14.9822 | -54.7328 | 2025-08-16 14:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| aca80125-a11f-3acc-8fa8-a3254b95d498 | -6.5638 | -43.0357 | 2025-08-16 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| c088aa01-fe86-3a97-b89a-2b4603267c7a | -7.9623 | -63.2407 | 2025-08-16 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 614d5090-8cdf-35d3-9a21-43037ea3d10e | -13.1267 | -57.1293 | 2025-08-16 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| ef9d0d5d-2e26-388a-94b4-d4cce2697358 | -8.9708 | -61.7033 | 2025-08-16 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| dc37fd71-975c-3261-ab98-33b03daf8821 | -7.6296 | -63.3273 | 2025-08-16 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f2d445e2-600a-3468-a643-af3105c72b47 | -7.9439 | -63.2225 | 2025-08-16 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 7d8ccb89-5a21-397b-adac-2f39bee5e811 | -7.9625 | -63.203 | 2025-08-16 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 23de3cf5-8e22-3406-acd1-890bbb55559e | -6.6233 | -42.7479 | 2025-08-16 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 91aea3a0-1115-32f9-a75f-47d3eae8b01c | -12.6143 | -46.9047 | 2025-08-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c71fd100-5641-3ffe-9f1e-e4c3fe4e0bcd | -6.6045 | -42.7496 | 2025-08-16 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 80a7cab9-519f-3485-971f-e5308f6e9408 | -12.6139 | -46.9273 | 2025-08-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| c6fc9eb8-36d5-302f-bb77-f72f02fab600 | -14.9628 | -54.7351 | 2025-08-16 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c5f22ae6-1f3e-3d87-949b-f924ea742a19 | -12.5947 | -46.9301 | 2025-08-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1995f68f-1069-3fb2-9791-0208e5738edc | -8.1061 | -55.5501 | 2025-08-16 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 23df45f9-601b-37e2-8a8a-18f70af79e7a | -6.9276 | -44.1666 | 2025-08-16 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 578fe306-117c-3501-b17a-5c7382cd0fa2 | -8.9893 | -61.7024 | 2025-08-16 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 1c7cb7f4-c521-3403-815a-04a4c83ae4e5 | -12.8234 | -45.988 | 2025-08-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0079289c-e081-3cd7-a34b-4b7e4d550e99 | -6.6042 | -42.7732 | 2025-08-16 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| a6e66e27-320e-31e2-a6c7-203a4e69e588 | -7.6295 | -63.3462 | 2025-08-16 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0ed43b88-4736-3b88-be50-402e6a316e26 | -12.8418 | -46.0309 | 2025-08-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 4215b91d-e472-398a-9b08-6ef031956af6 | -14.312 | -53.2291 | 2025-08-16 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 04bd66cd-f8d9-3d66-8097-4c183b161cf4 | -6.5641 | -43.0122 | 2025-08-16 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0f2648cc-048e-39c4-bc69-84d60bfefeae | -12.8045 | -45.9681 | 2025-08-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 39a6d490-fce8-3c85-8a93-a4b3585c6a52 | -7.9624 | -63.2218 | 2025-08-16 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 212.8 |
| 0d812b7c-b8e9-3910-a2c1-207962060f06 | -7.9624 | -63.2218 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 237.9 |
| a8a9b71d-dd6b-3af0-9939-6a4152e66d82 | -12.5562 | -46.9357 | 2025-08-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 42bf5641-083b-344c-9012-d6f96f82dde1 | -13.4577 | -47.071 | 2025-08-16 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5d7563ed-268e-3cd2-b1e8-c1de974facb3 | -14.9441 | -54.6959 | 2025-08-16 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9730ab39-7901-3685-8f6c-2682804270ca | -7.6112 | -63.328 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6f76eb41-0119-3b0a-acc8-9217fd4d3854 | -6.5638 | -43.0357 | 2025-08-16 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 1683d31e-b5a6-3d0f-b2c1-d939ff661ce7 | -6.9276 | -44.1666 | 2025-08-16 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| dc117c67-6901-31d8-a0a6-1e0975df9d6f | -8.9709 | -61.6842 | 2025-08-16 14:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 60c87765-32b4-3322-940d-a242203ecac0 | -12.6143 | -46.9047 | 2025-08-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 33292449-6076-3f7d-8875-8ddb98a9739d | -9.6906 | -46.2735 | 2025-08-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d4f5a8e9-9cf4-3917-9a71-7cf90d17088b | -5.9134 | -44.3196 | 2025-08-16 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d81cee80-0f72-3a52-b0aa-87c69405095f | -12.6139 | -46.9273 | 2025-08-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 58d6cd89-8d7e-3182-a89c-4b52b1521182 | -7.9623 | -63.2407 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 941738a4-66a2-36e5-b87d-2b02c4660d28 | -6.6045 | -42.7496 | 2025-08-16 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 76cae7d4-7181-36f5-8533-270102115534 | -11.3657 | -55.4107 | 2025-08-16 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 53618ee6-1bb5-3ca9-b512-b57bfd117c7f | -7.9439 | -63.2225 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 5589f32c-6eed-3312-a998-9eb43e255664 | -15.199 | -51.1527 | 2025-08-16 14:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 51020eae-4f09-3c27-b95f-71405faba6fb | -7.6296 | -63.3273 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 7741ee2a-a975-3536-b01f-11c2341f2070 | -14.3344 | -53.0372 | 2025-08-16 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 1a0233e5-e36c-3f8a-8c89-151b9e855258 | -7.3891 | -44.9046 | 2025-08-16 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1d24d4b3-da4c-35a3-babd-f194f268a99b | -14.9825 | -54.712 | 2025-08-16 14:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d85862b8-bd24-3f6a-a722-b8c978cc150f | -13.1267 | -57.1293 | 2025-08-16 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 2c127063-eaba-32eb-842d-722455388ca0 | -14.312 | -53.2291 | 2025-08-16 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 135d4009-27ec-324d-870e-220329ca8f86 | -7.6111 | -63.3468 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f4405956-1263-3695-8819-f62adc8f88d8 | -6.5641 | -43.0122 | 2025-08-16 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e9ca814f-a226-3e03-b8a1-802c9f3a46e2 | -6.0978 | -44.6261 | 2025-08-16 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b626d76f-586e-3bd8-b9e3-c71bdf4b8a5f | -7.9625 | -63.203 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ad28f720-df35-369b-b1b5-ba9ccae023a7 | -6.6233 | -42.7479 | 2025-08-16 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 5b4a01b8-54dd-3283-b214-a202a05cc577 | -7.6295 | -63.3462 | 2025-08-16 14:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| f1e12799-2957-3789-a4bd-866998b622cc | -12.5947 | -46.9301 | 2025-08-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 80713dc5-eab5-3420-9734-6654c31617f6 | -14.9822 | -54.7328 | 2025-08-16 14:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 3ef69daa-db6d-34dd-9789-392314659681 | -14.9628 | -54.7351 | 2025-08-16 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| d1fd307a-16a5-359b-9c2c-354815a8ac37 | -11.6607 | -51.6221 | 2025-08-16 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 032a5c0a-cc7d-3e27-a933-1ec1f581e454 | -8.9709 | -61.6842 | 2025-08-16 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 40aa2b13-dade-394e-ae6a-ee9be573e87e | -8.9708 | -61.7033 | 2025-08-16 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 8a0644fd-dccb-3a2d-ac69-3189e9d1df47 | -7.9439 | -63.2225 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 63314069-8550-338d-83e4-17dd0d51e544 | -13.1077 | -57.131 | 2025-08-16 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9cf82bfa-b6e0-3fdc-828f-bf3a42a23169 | -7.6112 | -63.328 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| f2402802-7d31-36f3-a267-c053551b9da4 | -9.6906 | -46.2735 | 2025-08-16 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| df9b48e9-9e8d-321c-b321-25964b199bc7 | -13.127 | -57.1092 | 2025-08-16 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ba3f4587-93a2-3189-b116-b2837370f6ff | -8.9892 | -61.7215 | 2025-08-16 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c4dc84a9-9e9e-304c-aeac-140d1184c313 | -12.6139 | -46.9273 | 2025-08-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| f7ca3aed-219d-3d3d-9dba-edb53ea2e1d9 | -14.9825 | -54.712 | 2025-08-16 14:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 706e8126-af70-32cc-8644-00dd721d5df0 | -9.8125 | -45.6942 | 2025-08-16 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5fe24252-298f-3a41-bbb3-6c2b9446b1a3 | -7.9623 | -63.2407 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 32fda62f-ba8b-3f35-bf50-1d34380ddb94 | -13.1267 | -57.1293 | 2025-08-16 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 310942d1-5331-3c5b-945e-5fe069c86146 | -6.5638 | -43.0357 | 2025-08-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| ac46110a-946d-3ffd-88bb-73328580b414 | -7.6295 | -63.3462 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 39a94407-f198-3768-8558-7075cb39533a | -6.6045 | -42.7496 | 2025-08-16 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 4615084c-d7c7-3474-a702-9daff6ca29b0 | -7.9624 | -63.2218 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 180.4 |
| b8fac7fe-09a5-3422-aaf8-1ed4fdeae53a | -7.6296 | -63.3273 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 7099a349-50c3-30f6-a95c-e970372b343c | -13.4577 | -47.071 | 2025-08-16 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a2569dfe-260a-362b-940d-afe0adb79b01 | -7.5018 | -44.9169 | 2025-08-16 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ed3cd914-945f-3cfd-bbf0-1b896a6a872f | -12.5562 | -46.9357 | 2025-08-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c09563b9-d20d-3298-9c34-a85de253e273 | -7.9625 | -63.203 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2abd7b67-0441-379d-8f1e-cb0fc45e3a77 | -14.9822 | -54.7328 | 2025-08-16 14:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 424.7 |
| e75a301a-ceb7-319c-ae12-b02d28caa0c8 | -7.6111 | -63.3468 | 2025-08-16 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 02848625-96d4-30c2-a4fb-5069786089f7 | -12.5947 | -46.9301 | 2025-08-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 36003dc8-82e0-355a-a3c5-ceb8e16a70fc | -8.9893 | -61.7024 | 2025-08-16 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 152.7 |


[Clique aqui para ver as próximas entradas](README81.md)
