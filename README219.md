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

## Dados Diários - Página 219

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f921b13-66f9-3a1f-b90d-071511a13f0c | -9.0516 | -67.8525 | 2024-10-03 14:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| a8936bd4-de49-352e-ab1a-7acb3d667499 | -8.9976 | -67.4094 | 2024-10-03 14:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c3f74c48-dd50-3cc4-93bf-bf8c860c739c | -9.2573 | -43.4771 | 2024-10-03 14:35:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 833d87df-fd70-39b8-b2f5-305bb10f4f7c | -9.0515 | -67.871 | 2024-10-03 14:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| f3c64eb8-9538-3d4d-bbe0-187947bf5980 | -9.0149 | -67.7423 | 2024-10-03 14:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 031f8466-949a-3725-877a-338e08a82d45 | -9.5775 | -46.2414 | 2024-10-03 14:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 538a950a-0499-37a3-9753-41cfbc6f4622 | -9.5772 | -46.2639 | 2024-10-03 14:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 2dfd2f08-962d-3e1e-9cc6-32f77a1a56db | -9.3833 | -68.3256 | 2024-10-03 14:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 181.4 |
| 58780c28-645d-3966-883a-936da3c15469 | -9.5824 | -50.1797 | 2024-10-03 14:36:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c1d29022-4236-3ad2-b646-8b6c5963cb06 | -9.5821 | -50.2011 | 2024-10-03 14:36:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 26f2e561-89b8-3f6a-9ccd-40ae55c7f476 | -9.3834 | -68.3071 | 2024-10-03 14:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9e4097de-5d5c-3ced-912d-e3b745d27be8 | -9.3832 | -68.3441 | 2024-10-03 14:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2395eaf1-e1b9-3e0f-8b40-3ecaf2b041ad | -9.4368 | -64.5419 | 2024-10-03 14:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| a6109a4e-661f-3be8-83bc-c63385a0c8dd | -9.3648 | -68.326 | 2024-10-03 14:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 15ecf014-2c87-36a6-83bb-6e516b0f6a5e | -9.4018 | -68.3252 | 2024-10-03 14:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 80.4 |
| beac2b9f-6a9f-3354-8a92-6cc6a200e9a0 | -9.4018 | -68.3437 | 2024-10-03 14:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 07066326-27cd-3752-b0b5-a4a9f863b358 | -9.4752 | -68.5639 | 2024-10-03 14:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 99b40d0d-80f8-38e9-8eb5-596346a2f280 | -9.6012 | -50.1779 | 2024-10-03 14:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9b660522-7b4a-3f99-be8e-9ccb7f57783f | -9.4566 | -68.5643 | 2024-10-03 14:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ea526de4-e399-35c1-a7d3-cb425432caef | -9.4567 | -68.5458 | 2024-10-03 14:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6ce3fbb9-827d-30c9-9ecf-dd135bb428b7 | -9.494 | -68.4895 | 2024-10-03 14:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 41.9 |
| ded247b7-9ba2-330e-90a6-83b0cf57e66d | -9.4753 | -68.5454 | 2024-10-03 14:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 1e4643e4-6a98-37b8-9422-bd1b97b41723 | -9.7541 | -64.2853 | 2024-10-03 14:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d8b1b668-4b1d-3f92-a66e-ae394b311d40 | -9.754 | -64.3041 | 2024-10-03 14:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 311e5d1f-d67c-3667-9d1b-a8aba9c7009b | -9.9747 | -64.7661 | 2024-10-03 14:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f4eab6b0-e21f-3414-ad9e-aca12201178d | -10.0415 | -48.2316 | 2024-10-03 14:36:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 9b84b23d-f827-35c2-959e-261c5dfa62e0 | -10.0418 | -48.2097 | 2024-10-03 14:36:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 248.4 |
| 2c4549ad-0109-3a3c-9201-f5314429cce1 | -10.0229 | -48.2117 | 2024-10-03 14:36:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 467df583-3764-3f28-b237-620c5fefe6fa | -10.0226 | -48.2337 | 2024-10-03 14:36:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f03edd24-73dd-3342-82e6-b6c7f54b0d9e | -9.888 | -67.3485 | 2024-10-03 14:36:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 70c74b3c-734f-39ec-a1d2-af40c8ab477e | -10.2195 | -47.6839 | 2024-10-03 14:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 12d0478e-f4f0-3af3-8ccc-4f49249a670c | -10.5736 | -48.0839 | 2024-10-03 14:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6ef270bd-b1f0-36ed-84ac-b13671ba9609 | -10.7161 | -46.1942 | 2024-10-03 14:36:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 14629442-232b-3838-a32e-aaab15154dab | -10.5926 | -48.0817 | 2024-10-03 14:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| dd6d1c98-bf45-3269-829d-99f7016bc08b | -10.6319 | -53.6805 | 2024-10-03 14:36:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a2f50ada-21f1-3d6c-b030-953c93239cd1 | -10.7352 | -46.1918 | 2024-10-03 14:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 73b8c074-2685-3f44-8ce6-7df9bcea4380 | -10.6505 | -53.6994 | 2024-10-03 14:36:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| cc046007-edc7-36d0-a9bb-8a8960e07c4d | -10.7348 | -46.2145 | 2024-10-03 14:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 3799bf60-8a68-3130-9217-03759cb5a855 | -10.7315 | -47.6683 | 2024-10-03 14:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 0973aae4-d318-3123-afdb-df234600df07 | -10.7319 | -47.6461 | 2024-10-03 14:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ffda4fce-f8dd-36d4-bdf9-3dcaa2c746dd | -10.6317 | -53.7011 | 2024-10-03 14:36:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d4e33de1-12c3-3867-831b-2cec8fe9c352 | -11.2959 | -46.8399 | 2024-10-03 14:36:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 4db186bc-ec52-3c92-b981-f51850f6718e | -11.9105 | -50.1447 | 2024-10-03 14:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 08a020a6-0b6b-3427-90ce-5cf4234a140b | -11.6238 | -64.1099 | 2024-10-03 14:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 95a5aef1-0065-3523-85f3-642704e6c66e | -12.0131 | -47.3263 | 2024-10-03 14:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bc4542c9-f0a8-3a59-96c1-9da734c00bb2 | -11.9483 | -50.1618 | 2024-10-03 14:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a3a48c94-d636-303d-ada0-bc1893e25667 | -11.9737 | -47.3986 | 2024-10-03 14:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 0e88e72c-8354-3e16-a030-740f1840fe5c | -12.3934 | -50.9658 | 2024-10-03 14:36:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5a5f67f1-d756-306a-b8ae-1e94897e936c | -12.3292 | -54.0954 | 2024-10-03 14:36:16 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 58f554f4-cd13-3bd3-96e5-8d3b6b108938 | -12.552 | -53.1191 | 2024-10-03 14:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 03c6c97e-e911-3d20-ae5d-01f0c6dbbedb | -12.5332 | -53.1003 | 2024-10-03 14:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d28624b8-5118-36c4-b58f-8a6629b3ce65 | -12.9831 | -51.129 | 2024-10-03 14:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 2db34942-8138-3f73-b233-bfe005f32850 | -13.0402 | -51.1432 | 2024-10-03 14:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.0 |
| e506346c-2d5c-36b7-a3c6-baf7b5ff682f | -13.0406 | -51.1218 | 2024-10-03 14:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 33a87f83-3480-38dc-b94d-6000d65ea39a | -13.1787 | -48.6295 | 2024-10-03 14:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 11501802-c6df-3461-b9f5-3e05eb17bddf | -13.5195 | -51.1467 | 2024-10-03 14:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6827a906-8d4f-3292-9e1b-4b768d437605 | -13.5387 | -51.1442 | 2024-10-03 14:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| a9e539ad-7991-3baf-953a-212c8ead6079 | -13.6342 | -51.1746 | 2024-10-03 14:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 183.0 |
| a2e3f30d-5b77-36c8-a6b4-b14d37200fa1 | -13.615 | -51.1771 | 2024-10-03 14:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 7f889cd2-31de-35f5-98c8-6439ee4f28e7 | -14.0392 | -45.0947 | 2024-10-03 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 1e4c35a6-2891-3321-9c81-3d7edbb834e4 | -15.143 | -48.0819 | 2024-10-03 14:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 033ccd42-d32c-30a3-b08f-3f4d49a8ab48 | -16.109 | -53.5215 | 2024-10-03 14:36:37 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a62a4cbd-cdd6-3391-96b4-b324efb9ffd5 | -17.2497 | -43.1716 | 2024-10-03 14:36:42 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 996a53fb-ade6-3a10-b403-ac29262ad075 | -17.249 | -43.1962 | 2024-10-03 14:36:42 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4ee7e513-9000-3c07-a768-af271e17be51 | -19.0141 | -43.1998 | 2024-10-03 14:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 170.4 |
| fe167d9a-ebd2-377c-a084-bc7c171d9ae5 | -2.9836 | -44.2806 | 2024-10-03 14:45:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8824f60b-cee0-32a6-83f0-2063fdb528ec | -3.4296 | -44.4451 | 2024-10-03 14:45:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 222a35a3-6b91-3799-ac6d-bf06f31b7016 | -3.3084 | -42.691 | 2024-10-03 14:45:25 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b6355256-4534-3906-9edc-efe85e386d0f | -3.4728 | -43.3609 | 2024-10-03 14:45:26 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8da4eb38-4775-3b75-8cd5-097d6a649ecc | -3.8042 | -44.1072 | 2024-10-03 14:45:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 62cf3f22-f70d-3c75-8113-4ba9fcaeb147 | -3.8101 | -43.1116 | 2024-10-03 14:45:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7ffe2eb2-000a-3828-a405-61ae4266e7ba | -4.5375 | -43.304 | 2024-10-03 14:45:32 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4d33f47a-2743-3074-9807-6108f39db904 | -5.9271 | -42.8547 | 2024-10-03 14:45:39 | GOES-16 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| c065ad4e-3198-3ff9-976f-a59885a50261 | -6.0048 | -44.5647 | 2024-10-03 14:45:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 483ac75a-cc79-3a98-a558-1e225a33b7ad | -6.3008 | -43.0351 | 2024-10-03 14:45:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 10dcf500-0437-3423-9130-93744ce1f041 | -6.325 | -44.3791 | 2024-10-03 14:45:42 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 95b765b8-c7b6-3493-a65d-4ee31aeb922a | -6.5239 | -45.1162 | 2024-10-03 14:45:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c4705c87-c559-32da-81dd-944bacb25851 | -6.9479 | -47.6668 | 2024-10-03 14:45:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7c09beac-ff0a-3aa5-9582-82bb5f721fb3 | -6.9075 | -44.2836 | 2024-10-03 14:45:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 9a67c2f0-9a6b-37df-8052-dd60b5440992 | -7.651 | -67.2009 | 2024-10-03 14:45:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 00a11745-6bde-3ce3-9f5d-8b01fcd7a74f | -7.8149 | -45.4782 | 2024-10-03 14:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 06193757-9e3a-32f7-9161-e3e11d48c1bc | -7.7213 | -45.4418 | 2024-10-03 14:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 86b60f6b-bb28-3c9d-91e1-8ed642942466 | -7.7216 | -45.4191 | 2024-10-03 14:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 00a11651-5ab4-364e-a6a8-29e2929db5ce | -7.8406 | -61.7887 | 2024-10-03 14:45:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b6ca1c8f-602b-33d6-a5ac-2b7333747d8a | -8.194 | -46.8102 | 2024-10-03 14:45:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 83cec2f6-15f0-3af9-b154-a538173096f6 | -8.157 | -43.6977 | 2024-10-03 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 171.1 |
| 466a00d9-f3ce-3b33-8460-d23a9fc02cfc | -8.1759 | -43.6957 | 2024-10-03 14:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| e1c310b9-2cca-3e56-be79-15ce536fb4a9 | -8.1859 | -44.3901 | 2024-10-03 14:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 546d2f53-7ade-3ec8-ad08-34deb873c606 | -8.1937 | -46.8324 | 2024-10-03 14:45:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 9f708b8e-817b-316a-94cc-f2074ba2a9f7 | -8.015 | -63.7843 | 2024-10-03 14:45:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 07455160-1f83-3e22-a21d-4829909d10e9 | -8.2239 | -44.363 | 2024-10-03 14:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 5788ae02-4805-3165-a29c-534f445b2a06 | -8.1861 | -62.8364 | 2024-10-03 14:45:53 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a6514d46-f15d-38cc-9afc-9154bc9a3d7f | -8.3204 | -72.7839 | 2024-10-03 14:45:54 | GOES-16 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a2ca21a2-888b-371c-a283-c4feab85373a | -8.5582 | -62.4814 | 2024-10-03 14:45:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 56544b73-df7f-3bfa-83f4-c630e30a4bba | -8.7993 | -45.1044 | 2024-10-03 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| a4186e53-9ffe-3b5b-85cb-874f46b701aa | -8.8745 | -49.6471 | 2024-10-03 14:45:56 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d1c0c45b-c097-3164-b0dd-8ff2fe7b8e7d | -8.6493 | -66.6025 | 2024-10-03 14:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 57b76bb3-7414-3c18-a28c-7e570a90092e | -8.6675 | -66.6762 | 2024-10-03 14:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b0e9311e-b14a-3749-b7d0-7b5fbf3fe596 | -8.799 | -45.1273 | 2024-10-03 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 341301de-f08f-35bc-bc0f-ddf8a1f2b89b | -8.8186 | -45.0794 | 2024-10-03 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |


[Clique aqui para ver as próximas entradas](README220.md)
