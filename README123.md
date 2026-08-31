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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16a6eb87-faa9-314c-ac42-dcc5615b2468 | -10.14266 | -45.68515 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| dbbe0712-71a8-3526-a037-ad6eacc47f84 | -8.86588 | -47.0911 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3d95b4cd-b7f8-37d1-9260-4e091fd9d9c9 | -8.87706 | -46.03046 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3c3c0597-396b-33a3-99b7-3cf9996a3fc1 | -10.75158 | -54.04404 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| fc965e15-7dad-3afd-a765-cac23970d216 | -9.58757 | -47.62939 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a9e6e284-846b-306b-a49d-6da7f63a7881 | -9.42776 | -45.68369 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7b296744-ed35-3c5f-a700-8dbe30800560 | -10.08649 | -46.61782 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5326a13a-b371-3fee-91a7-74731b98805c | -11.54455 | -45.48403 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2506329e-54b0-3d85-ac4f-4b6c37fdbbdf | -11.0585 | -47.11761 | 2026-08-31 16:30:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0a5fb9a-acf1-340a-b0db-fe574bf96f91 | -11.67622 | -47.60193 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 586c24d3-5093-3161-91a9-f037bc437672 | -10.84755 | -45.31345 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 967954ae-8792-3123-8b62-00aea566645e | -10.98628 | -48.39365 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4ef21d75-af0d-3e17-a2d3-3d9848e52bcc | -11.24283 | -45.14487 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| af612505-d91e-39d7-bdb6-56b4b0bcb119 | -10.1151 | -50.31473 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 1997e54c-17cf-39cf-b27e-a28fbf9295c4 | -12.38308 | -48.16927 | 2026-08-31 16:30:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b527a02b-6917-32aa-846e-67be30aab1e1 | -11.20001 | -46.11655 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 313.9 |
| 8634ed7a-b8aa-3650-9040-a5ca2185a68e | -8.38537 | -44.99068 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5926766f-82c0-3786-a17f-ea380bb4b5cd | -11.23397 | -45.37944 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d3f10ae-bff0-3db4-bf58-0296c723511a | -12.09954 | -47.14925 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 2e43d3dc-8a5e-3a48-94d0-c1aa8b393f16 | -11.2162 | -45.09026 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48f2ac85-2552-399e-b261-7af1dad68ff7 | -10.12494 | -50.31038 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| baf943c4-295d-32c4-b442-b45d0ae79a9b | -11.24819 | -51.26614 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e83d9681-ee70-3d05-8949-d816ab6ec43a | -9.66936 | -47.94503 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 851b8508-a856-33a3-ac07-c6a022a71a57 | -15.26131 | -53.88583 | 2026-08-31 16:30:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3027b4bc-8a9d-313a-8155-ea4e00f1117d | -12.08943 | -44.99219 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 0cf84c8d-0106-3484-aa1e-2eaddba6032c | -11.16088 | -45.0446 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ddc8232c-470d-3262-be06-4672be588096 | -10.755 | -54.07207 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a60d8ce9-aca0-3f54-b5c8-46ed71ce567a | -10.18651 | -46.83948 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7473ea5-0bd8-3646-a675-9c12103499a8 | -10.10998 | -50.3154 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b519a68e-2278-3a7e-8d4e-5ee85fe59ef0 | -14.95072 | -54.57617 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f0876a54-b926-313c-af9b-ac63f7b0c888 | -12.08827 | -45.7518 | 2026-08-31 16:30:00 | NPP-375 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8975b9bd-2708-305b-9967-d7760f8a1115 | -11.92584 | -45.08294 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f73b373f-550f-32d2-9179-9f5332d57615 | -14.54641 | -51.97973 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4081b8cb-7163-3b14-b336-498d7a150fda | -11.20574 | -45.09624 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 437e3bdb-f145-3900-b71e-312f7f1c52ff | -10.12454 | -50.30736 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c5b0d750-1044-3ed2-bc1c-ce497f8a0e40 | -11.96332 | -47.74772 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| e027bd74-3f86-3211-a77c-51ae6e32fe8f | -12.75735 | -49.27996 | 2026-08-31 16:30:00 | NPP-375 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de27fc98-0777-3d8e-876c-a65f763c8d8b | -9.58812 | -47.60143 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e923d20f-cb5d-368b-9b4b-41dd5f1f55f2 | -12.18921 | -50.51932 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 796f72ae-edd5-35cb-bd41-db69535f4add | -8.77053 | -46.46027 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 86c34f74-4d52-3fba-b958-6dfe0316b112 | -14.59337 | -53.60801 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d1c14e35-622a-3e8e-8b6a-2b5b10f5de63 | -11.20943 | -45.09569 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d8f83625-f317-3d0b-9f62-1b8264820a69 | -10.11906 | -45.84576 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 169e8634-6d84-3993-a7ef-6757d8b57fc6 | -9.42675 | -45.68176 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ea660b19-e200-36de-9ce6-449ebed300a6 | -8.92772 | -45.03951 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d5ef1cb4-2987-3611-905a-f9648a0b4631 | -11.21828 | -45.34906 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0189b20d-31e5-3a83-b61a-0be20296af04 | -11.22482 | -45.09783 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab47d29b-883d-30e9-a58a-5ba9a624ab63 | -9.5918 | -47.59689 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5d75cdf4-d125-3cbe-8bc5-dd15e788080b | -10.04335 | -48.68718 | 2026-08-31 16:30:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a7133a1c-e2dd-38d0-aa3a-9912dfeb0fe6 | -11.25013 | -45.35809 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 984e1b61-c3cd-3f50-96b4-2011e0069917 | -11.23742 | -51.26058 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a16bc73f-36aa-3ae9-acb3-d6db7af1bda2 | -11.19864 | -46.10641 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d27d15ec-605a-342e-9773-42b836f153b8 | -10.73381 | -47.96121 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 07103823-77a7-3e4a-b284-e1a7f2f6c5d9 | -11.32659 | -45.16613 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 78d31ae6-da24-3cfb-b564-0ce748e2e02a | -10.12612 | -50.31945 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89df5ced-5904-362a-9c8e-e8007b2408ba | -10.7477 | -54.0669 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1c114d10-1d04-3119-b282-5894ef4b2a9a | -10.16428 | -45.72857 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1692a1bf-eee7-3330-8988-80b36bfdf759 | -11.68693 | -54.55128 | 2026-08-31 16:30:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 09f70302-a14a-38b3-8d76-958b565efc1c | -11.37675 | -45.17226 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 99f53178-ab82-31d1-a23a-1662179581a1 | -11.23109 | -45.1421 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7e0025f5-a1e8-3814-a3b9-f2c2cf250899 | -8.42506 | -44.98848 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fbce8cc8-372b-3c04-aaef-22dd91ce34bf | -11.20798 | -45.33569 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae086e0c-9842-3acb-b8d4-27fe5d3d490e | -11.37437 | -45.20875 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 1f66e94f-4758-375e-9642-32bca3f67b71 | -10.84523 | -46.00077 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f2d65e92-2023-377b-8ca0-5cef515813ca | -11.93262 | -45.077 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e338fb18-a03b-30fc-b30c-5e9a61d4c820 | -14.4767 | -49.04029 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 50078df1-8f18-3a3d-8d2b-4a267ab6a5e2 | -12.07735 | -42.54289 | 2026-08-31 16:30:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8e928d6-e2a5-3740-98a2-d7740dd72cb6 | -9.5839 | -47.60204 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 257e219b-fc4a-3cc7-839b-ef288b1db71a | -10.33867 | -49.96559 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ad59dd85-b74a-3881-839e-4692385d2cbb | -11.21192 | -45.11335 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 38ff7647-e770-3558-9111-53fddae1b46b | -9.67579 | -47.92767 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bb32200e-b4d1-3b0e-8e80-a0988f97c44c | -10.34446 | -49.97068 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 71bf72d7-a3e0-3914-983d-366ba8c2c1dd | -11.24653 | -45.14433 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 22bcfcd7-9cc7-3628-98d1-6d259df4fa34 | -11.85132 | -46.76228 | 2026-08-31 16:30:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e1a93a1-656c-3890-bb59-223d90518f95 | -11.19541 | -46.11211 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 6358b768-c8de-374a-a100-36193986fee5 | -9.64691 | -46.06184 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 98a2356b-7b9d-3b0c-b57a-e6f98ad2b608 | -11.19961 | -46.10909 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a2e8474a-65f6-3a19-b642-ccc9892c8229 | -14.23903 | -51.94397 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 99443bd3-33a0-37b4-92b9-bdd4172ed3a5 | -10.93125 | -46.61112 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2ce302b8-139b-32f8-8337-7626fc10cddb | -14.64007 | -53.57372 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 9f847f5c-0e57-35ca-b88c-710187f6eb81 | -11.19932 | -46.11148 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 6e3f5fb8-f908-3e55-b718-c5ddb2cb40ae | -11.21392 | -45.34513 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3f779f0-accc-34a0-a1dd-276f30ae8a12 | -10.74934 | -54.04195 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b4f4cd96-8fcb-30af-a1fb-2f8fb4ff8f73 | -11.92646 | -45.08743 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dd05d98a-f043-37a9-a685-e970aac4cf57 | -12.95851 | -45.94341 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| c7d33ab1-97f2-3d24-8ded-eacc4766ac23 | -9.20343 | -47.99432 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d55c205f-bb7a-3fee-85b6-722c07287ce2 | -12.09525 | -45.0601 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 38954512-4738-3471-a344-2749f941a6b5 | -8.7614 | -46.45174 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d591c120-02c7-3353-8236-895059d2d3f7 | -15.26754 | -53.87885 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 621bdb8f-2401-346e-a82f-a37a61cc5e7d | -9.1641 | -40.11111 | 2026-08-31 16:30:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f6226e63-968c-30b1-a2d6-93451e53475a | -12.09654 | -45.06923 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 08b992bd-4219-31c5-af30-ee087ddfc0b3 | -14.96569 | -54.58294 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| dea2904a-5335-3109-b45d-c2ca3b7a544c | -12.07238 | -47.20024 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 485242eb-78f6-30c6-b0e9-8b2b995c72c3 | -8.6446 | -47.30838 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9e31366-3afb-3ca5-8eab-01cbebe78a14 | -11.91357 | -45.04903 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b97accdf-3c33-3338-90c8-72edc178b496 | -11.51674 | -41.69727 | 2026-08-31 16:30:00 | NPP-375 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9267156b-28e5-3f91-9e62-970277b7bd0b | -12.32908 | -41.04403 | 2026-08-31 16:30:00 | NPP-375 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a808af09-ac28-3572-a554-7cce6b666a23 | -10.45159 | -46.75619 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8fee1468-590c-31a8-8bf4-85b213efe5ec | -10.12602 | -45.8401 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2cac8479-5c76-3b93-8fbe-516c3cb1d2e2 | -11.19465 | -45.04425 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README124.md)
