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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cb445ff-085a-3633-9975-662cf6d53483 | -11.10299 | -51.98302 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfd81ec0-d4dd-334c-a50d-65704e5b60be | -12.10662 | -44.86147 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6fcd75e-aed8-3e16-bf52-c227484e4119 | -11.67655 | -46.60032 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ad08736f-a673-3906-9d67-1e129957300e | -9.11176 | -46.95848 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b934353-2df9-3a4e-be2d-cf109dc5b40f | -11.68314 | -46.53563 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b98e87ea-c68a-3b9b-bbad-09e8d8059a93 | -7.56489 | -44.37622 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e29476b9-e9c7-3689-9de8-90aad9e6be91 | -9.71822 | -48.30616 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1a3473b1-9d5a-3bbf-9ea4-66b4ef1674a4 | -6.44678 | -41.76464 | 2025-09-12 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 47451d58-3a5f-3f0e-8534-b096b07877c5 | -5.29215 | -48.12535 | 2025-09-12 04:25:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 873e4324-8159-3833-b477-9241e2fe5f9b | -10.32711 | -48.80875 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5baca82c-6843-3583-b33e-9d6aa8ceefff | -10.55284 | -51.52712 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4cf4894d-2baa-361f-a70b-a171411e340f | -6.63133 | -49.78588 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4dbed15-0aa2-3236-b6e0-7e49a4452072 | -11.4933 | -43.64064 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1caf1433-ee57-3034-8166-b0e703bc79ee | -9.21148 | -59.37841 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22a38426-2ff1-3ef5-8717-c90a58e06c08 | -12.15185 | -43.70657 | 2025-09-12 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b97d053-5879-3d63-8098-7406c5997152 | -11.67824 | -46.6115 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d07e5a5-7b04-3c80-8578-55e9e1302aa6 | -7.32618 | -44.60866 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d21889a-b80c-35aa-a270-459b0038b519 | -11.53607 | -50.40336 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1e03a51b-8d4f-3fad-a2e7-18b309916100 | -12.11899 | -44.85094 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41639add-1216-324c-8510-bbe65a923f7d | -11.67154 | -46.58854 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86aa170e-a171-3d30-aeb9-74f25e62fb88 | -11.75405 | -48.26558 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 362a4e7a-0f86-3b3d-bc1b-a53e7b9e4aed | -9.09685 | -46.9454 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510e3e40-3ed8-36d2-b1b7-1f6228dd3ba6 | -9.04342 | -47.06881 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc523363-439d-398d-8ebf-fb9309c5e552 | -10.42756 | -50.62356 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81450b45-1f08-301f-a19d-973e81066723 | -7.45983 | -44.42209 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b851b1f6-2f4a-37a1-a1db-7bf50f59e2b9 | -6.95956 | -44.82766 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87f55b93-956c-3a8d-8819-a3aecdd42d8f | -6.2859 | -42.40098 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a71321a1-cdcc-384c-83b9-3d4b1e6d54d7 | -4.89959 | -49.923 | 2025-09-12 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2861013-e798-3952-b747-f2bdb194d5ab | -8.31241 | -44.88931 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3689945a-8449-3557-9001-99e904ab52d2 | -6.83689 | -52.79784 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e43ad49e-042d-35ba-8b6b-599ec1dc397d | -7.85232 | -46.06964 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb827efa-07ae-36b6-b343-38241e8c54ac | -9.45757 | -47.64808 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58be471d-a223-3921-86b9-83950ce2ed39 | -8.88033 | -49.93916 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d777b3ff-19d0-39d2-9032-7a57df9750f0 | -7.86094 | -44.84028 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84831db1-e7cf-3b29-b0ce-d9ec13a1711c | -7.52974 | -44.67366 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baf6df55-3aa9-3d81-af20-1fcd89e088b6 | -11.67482 | -46.54524 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da449be2-bad2-38a2-8959-570fde4ab691 | -10.53454 | -51.51864 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b51baa65-44ad-346e-9d51-399385c55ba1 | -11.68651 | -46.55805 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02f96f80-3c81-368b-ab8d-68512a62f1c2 | -6.80953 | -45.63847 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c8a1767-253e-384f-9e9c-1451a920b338 | -6.94881 | -44.78502 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e9ec073-fe61-3e60-b375-3492cbdae50d | -10.96348 | -49.57024 | 2025-09-12 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f8296d-0988-3e83-8f86-9029fd09c6ec | -8.37839 | -44.84636 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b471e448-145b-32ec-a5a8-170e992595e9 | -8.88169 | -49.93085 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e98eba2-4032-31c4-b2d8-4ad27607b390 | -7.7175 | -44.79596 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7411970f-86ef-33f0-ac16-fe325ca8e07a | -6.84491 | -47.87419 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 685cc0e4-e518-37f5-87cd-f8ea256adba7 | -6.76826 | -41.59398 | 2025-09-12 04:25:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 00fff44b-09c7-3801-b95f-db2282718475 | -11.74058 | -43.37555 | 2025-09-12 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f9565bb-026e-3815-9736-8380dd90fb55 | -11.48263 | -49.27274 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fafa8bcc-bc0a-3301-b0fc-9021c98d0f39 | -6.45035 | -44.06817 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 151a2db0-d993-3ee0-ad7b-865e4633738d | -6.67473 | -44.15134 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6926db12-e240-3153-8455-2cef6608cf02 | -12.0786 | -47.59092 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5525a1a0-4f35-3b21-90c4-af5c43e998d7 | -11.67874 | -46.56411 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99956cd1-f826-3aa9-b004-a16d0736ed9b | -8.89471 | -49.94157 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f54dee7-0816-38a5-b03b-72a4e317d8f4 | -11.09519 | -48.41345 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| becb7b7e-8a40-3c7d-a1db-0e6c6a99ff29 | -10.40888 | -50.00888 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9e2e8b6-a4fd-3c48-a0cc-381965c6b2ee | -12.1019 | -44.86904 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc87df19-7184-34b1-bee0-85b835847a2a | -10.16818 | -46.17054 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd2771ff-93b1-3535-8d6f-4a5b7b97809e | -6.47844 | -45.15054 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0288e9b-6d67-3a88-953d-8819d7cb902e | -8.08231 | -42.56185 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 85dac86e-957d-333f-b327-8b320fffab04 | -8.40569 | -47.27721 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9700a125-5946-35e5-878e-fedff09f7573 | -6.55113 | -43.95795 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c87f78f5-cb3d-3d2d-9b14-66fdff65f166 | -11.53863 | -50.40285 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b2b34410-3fee-358c-9b2c-f7c86dc9680e | -8.89606 | -49.93327 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6ef4edbe-cbea-394e-b54e-f6130d3b7431 | -6.28446 | -42.40318 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e9e89ea0-2e01-393d-ad7e-76fd1087018a | -10.84647 | -48.16011 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1810aba3-0999-3251-b07c-96eb2a551ac3 | -9.06989 | -47.11591 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8b34e951-7ef0-3ca5-b0fd-22bd5b60491d | -11.65825 | -46.60827 | 2025-09-12 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3a3dde4-1402-318d-9ac1-2788c627cea4 | -6.96634 | -44.8287 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 206d38de-45a7-3206-a573-380cb8b487f8 | -11.46671 | -43.61377 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76e9fb7b-e5b4-3d20-9d47-296c25343928 | -8.88752 | -49.94035 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f72b555-bc38-39fb-9275-d39cd3f30110 | -4.4843 | -48.11602 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c2f28976-1a44-3996-acbd-cdcff0e26955 | -12.08135 | -47.59497 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8308fea4-14c6-3d6d-8c54-aa63569098e0 | -5.76795 | -45.5254 | 2025-09-12 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0b35769-20d9-319c-b2b2-3d0fc5addba0 | -6.88802 | -46.3938 | 2025-09-12 04:25:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0e3a362-297f-34e1-a1d4-f78c1d32900d | -9.95049 | -50.31669 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c22993-f851-3d1a-ad90-bde5c9bb4d20 | -11.74569 | -48.27514 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83725c7a-7860-3013-8deb-0950837a7c74 | -11.45261 | -43.57922 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13fdb95b-5f5a-382b-aea2-f8a3f347e002 | -7.21668 | -43.97932 | 2025-09-12 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807840dd-37fb-30af-8d4e-9b07fe6ad8db | -10.55931 | -51.48899 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6edcde0c-d3c8-39fd-83e6-4df49031a860 | -11.53186 | -50.59428 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 92be2c24-9e01-3440-8e0f-90f9f31d02a1 | -10.72627 | -48.3158 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e04fe312-d9e6-3bec-af37-3ee15546cf90 | -11.6843 | -46.57232 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c329daab-7d7f-3a83-bf55-c107d88affbd | -9.78018 | -47.85927 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 328c9354-1083-3673-a51d-ee9ec07c7048 | -9.14004 | -58.92199 | 2025-09-12 04:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc31fad-6306-3270-be1b-a73ad1e40f5d | -6.67878 | -44.1479 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dba3fb22-dd4d-30b0-b234-fd4eebf234a0 | -10.70765 | -48.62302 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e828f69-069f-36b1-9f5a-a238980255f3 | -12.13252 | -44.83261 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f071df0-cbc8-3d7c-82fa-d81854df3fcd | -8.89281 | -49.93978 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 266631d1-befe-324b-9f19-d93e9dfae8dc | -10.34776 | -50.54074 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15cf1453-f501-3aa6-9e9b-a7c7d7d7ca2b | -6.68052 | -44.13643 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ddb8520-c111-3bdd-8cbe-7b6997502cd3 | -9.83367 | -54.53122 | 2025-09-12 04:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 95a8d3e4-be2a-3a49-bc2b-26ad8968529b | -11.52612 | -50.60626 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b99e2eab-15d7-385a-b9d6-e0b5f18d4f68 | -11.75038 | -48.35265 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96f39221-de65-343a-a1b6-fc7d6abc476f | -12.07804 | -47.59443 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2982e071-4993-3c48-a149-467f69095230 | -9.67912 | -47.53654 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 000ac5ae-5c81-3492-95d4-f754fa4d3c06 | -12.54754 | -44.69112 | 2025-09-12 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a306e8b7-a4a6-3dd6-a987-f192e3dc64f3 | -5.86654 | -48.1538 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 289f3123-ae4e-3714-95a2-a37dcbed0bc2 | -9.06982 | -46.57686 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bbbe38a-a9ac-3e3f-9dad-079da5178581 | -7.85248 | -44.80489 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffab33de-80e8-36b7-9d4e-96017107b93a | -9.66638 | -47.55242 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README75.md)
