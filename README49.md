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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0932d97f-7788-3832-9a87-85008f347027 | -9.71268 | -48.61456 | 2026-10-06 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f59b1a55-770c-3886-9d8f-9c141d7c9f58 | -3.70589 | -58.9324 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 641960e2-c2da-354f-aee6-235f257a0be9 | -7.37971 | -46.22626 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 916f4400-03b9-345b-9a26-6e5151872f45 | -11.26598 | -45.51409 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 69446b71-9b43-3bf9-817a-3d786532a969 | -11.04953 | -45.6418 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9ce05ce-9d55-372c-a366-5f5274ef1539 | -9.50095 | -49.24221 | 2026-10-06 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d909fbd5-cab5-3507-9186-2bc7adb90eb7 | -9.43939 | -48.68893 | 2026-10-06 04:40:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e054e95f-652f-3ed7-bff2-ef2a9321b098 | -11.7724 | -44.92071 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d24b466-7044-38c8-a348-ef41c866012d | -11.2372 | -45.25869 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af348cf5-75d3-3b58-9a20-92495166447b | -11.26662 | -45.50965 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| d658b87d-ed5e-37eb-863f-2c548936af07 | -6.93267 | -43.67727 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a647542-4e3e-3a7a-9cc2-fc6e287ba231 | -11.27207 | -45.52408 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c7576bc5-3b59-31cf-b6ad-e35453564603 | -9.80872 | -47.82703 | 2026-10-06 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93b22e3c-98e4-3605-9c26-4d59c182da0d | -7.10323 | -42.54264 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51b597e1-f3b2-3391-91de-87e14ba9c5c4 | -11.66738 | -43.63335 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e37b49bf-41f0-3687-97e5-3e1097cfd2bf | -6.92848 | -43.67452 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d025dced-319a-3dee-870a-a2168d640f97 | -7.2587 | -48.06613 | 2026-10-06 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 820c6b6d-084e-3b5d-a418-3f2698415505 | -6.44435 | -55.44191 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 902bd21c-c128-378e-b46b-a25e1fc89b39 | -6.2133 | -55.67118 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d82ddb0-1b9a-3f2f-8045-07cbbe8edae7 | -5.89342 | -53.6379 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab793feb-e438-3575-bb93-5ad27af2789b | -9.82544 | -44.7952 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e466704a-443d-3cef-af53-01ce6c655d13 | -8.69825 | -45.20575 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cb15d8a-7187-3b00-a4b1-aff352e3bfc6 | -11.35387 | -46.65069 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b3e8d43-9d6c-3838-9acc-61e6861ee039 | -6.72 | -44.28091 | 2026-10-06 04:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e8bd983-1fb9-3d7c-b242-f9d7c6fd9bbc | -13.49369 | -44.3616 | 2026-10-06 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0624e734-2b7c-39aa-868e-343b01b1486a | -9.7634 | -44.79748 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c889059-137d-3305-b71b-7eb15063ad02 | -11.71825 | -43.64368 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc539728-148d-3256-8777-03a0090a99b1 | -11.36435 | -46.65987 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 957b1330-c71e-38e5-8737-5a14bc255ca5 | -4.35447 | -54.86816 | 2026-10-06 04:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0de8e867-7ce1-385a-a652-f50b7d6570ce | -13.02523 | -43.12318 | 2026-10-06 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f3aa3a92-54b1-3c1d-a072-c85ef267e770 | -6.34768 | -42.56493 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 858baeff-a03f-3f22-8a06-1353d70a007a | -11.72296 | -43.64039 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cbd4c32-e617-3c48-85c0-f5de7154b29b | -6.61831 | -41.56595 | 2026-10-06 04:40:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5ca15a0-e7a9-3009-8bfa-0b9fbdf8cbdf | -10.42401 | -49.24886 | 2026-10-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66bc4123-bdfb-3db3-8ccb-6e47438380c3 | -5.67375 | -53.49884 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d1fe6c9-f46c-3e13-9897-f809b50dce8d | -11.27532 | -45.5019 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5ff51f37-6ffc-32a4-863f-50b1090cff52 | -11.24162 | -45.2547 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75b3e06b-4bce-33e4-a92a-1b86655192ad | -11.29054 | -45.52685 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ff9d8750-0201-3d56-af60-697df0cbfdaf | -9.88221 | -44.80338 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19c18382-469b-3c0f-8525-9da7b75d1173 | -11.68743 | -43.65142 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abb4dd03-43ee-336e-98ad-91836c42c090 | -6.00565 | -47.39531 | 2026-10-06 04:40:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 63863378-4732-3863-9ea1-e36002788ba1 | -6.93236 | -43.67514 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1fda6203-bfd8-3456-804e-00e1d27820fd | -4.28868 | -54.80122 | 2026-10-06 04:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a7b1159-e8e4-3633-9e54-e59bc1864638 | -6.91886 | -44.56417 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14446518-0b95-3412-9bee-baeb4f0e8cb0 | -11.28141 | -45.51188 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7fb53dfe-e277-3d04-afa5-6c10272fef05 | -7.90528 | -44.19276 | 2026-10-06 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a49c9d30-2d47-37d8-aaf5-97333b5ad3ef | -11.68694 | -43.65511 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54736e6b-11f7-3592-91d3-bd9c50c16560 | -7.33968 | -44.37966 | 2026-10-06 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e9f2ccb-a53a-3c9f-b857-cd97d6f7582d | -10.53267 | -48.06166 | 2026-10-06 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7e9527e-99ab-385e-a697-2517b2073b02 | -4.45703 | -54.96007 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4c0d502-e8ae-3532-88f6-2435cc7cbe61 | -5.84071 | -45.01702 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9e15aaa8-5cd6-330d-b6c8-30ddc6971316 | -11.35677 | -46.65519 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4e69d12b-6494-3ec9-bd18-55c1871518b4 | -7.4743 | -42.80912 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9948bb65-4e98-3042-913d-5a6d06440ec0 | -5.75095 | -46.67982 | 2026-10-06 04:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 61d5ec43-a75d-35a3-bfcc-0d8e7a2206ae | -9.81034 | -44.79276 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc9db019-4b9b-3629-922b-af6a86207cf3 | -6.35051 | -42.54628 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb13d0a9-ad7e-3213-9dcc-f112abb2d6f5 | -11.35327 | -46.65461 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 606a31da-26ba-3d10-8f38-92dc70210b8d | -9.25868 | -45.65942 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 122a749f-7a40-38cb-ab88-a20faebb0402 | -5.84364 | -45.02161 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7b818ad1-fc4b-3670-8b13-c6b448b95d63 | -6.43171 | -54.71273 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5256c58-651d-370a-b818-6b3863fb9f38 | -6.89512 | -43.6847 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b0208b0-1e5e-33cf-8c1a-6e1b9a19b7b8 | -7.46675 | -43.00121 | 2026-10-06 04:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 206b1b0f-5dfb-3511-961f-5a35fc3bcaeb | -11.83511 | -43.54585 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2457865-cdb4-3f85-90a4-89373ab9f8b2 | -6.15072 | -47.12115 | 2026-10-06 04:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79b78432-1f7f-3234-ac45-a9353eb9a736 | -6.45002 | -55.44552 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f911772-c62d-3f56-bedd-a2e243f6c28b | -11.29489 | -45.52295 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 01adf345-d4e2-3578-9c49-20b29a922821 | -9.79965 | -44.78645 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65d7fea5-af0e-3637-a8ab-c72a51e89335 | -11.25923 | -45.50853 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d48a5bb4-521a-3d0e-99f1-701e21bfa596 | -12.76294 | -44.8735 | 2026-10-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9768e6ba-334b-3c08-800b-af817051ea2c | -4.28222 | -55.76304 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6f39cf1-b9f9-3221-8486-37c13f658356 | -10.94375 | -45.39467 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1122c59e-0113-3279-9fb3-1509a3e288dc | -6.42259 | -43.46779 | 2026-10-06 04:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78a94bb4-f16c-3bdb-9af2-b7bb73e69ea4 | -9.2557 | -45.65481 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 686048a9-63a9-33b5-a608-f799b364bca4 | -5.98563 | -47.06697 | 2026-10-06 04:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fbf3609-166b-33fb-a122-2f9b078e1948 | -6.34354 | -42.56426 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 61690d3d-440d-32e2-99f0-d007f88b5840 | -11.68563 | -43.62467 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 139b6d2f-689a-3a81-9c91-b77785986075 | -11.63438 | -43.65652 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97018ad0-00f6-388a-b987-0dd70cd5de14 | -3.54017 | -59.49244 | 2026-10-06 04:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc622d0d-14e4-3371-9545-c2f1ba4016ed | -11.3596 | -46.68367 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20e737e8-d311-3664-ad88-8746df3e053f | -11.63852 | -43.65728 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff076cc4-6daf-302d-a4ed-6f2f37e6a2d5 | -11.34629 | -46.65347 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3efc9fe-8932-3520-9379-b000e03c9eb9 | -11.36308 | -46.6843 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27a0efa8-5504-3f40-be5d-17858b7e541f | -4.27674 | -55.76502 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dd85568-aafe-369e-93ca-c6f1b4f5f2bd | -6.92384 | -43.67884 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0c6cd34-75a0-3114-9e29-820199b43765 | -11.28576 | -45.50796 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 716f118e-2de9-389b-98bf-57fb620526aa | -6.00162 | -53.50949 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddbeb2f0-24da-38fb-ab7a-fc3ce765a36b | -8.58428 | -45.65799 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d16c458f-2ebe-3984-ac9f-6fee3b9f5a6a | -6.8757 | -43.68168 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42280307-12db-3d05-9fc9-5c85f0365ab4 | -7.89837 | -44.1867 | 2026-10-06 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a44b089-7b2c-33a9-aa71-6de1d9bc1b17 | -11.72243 | -43.64424 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47977059-c8a0-3475-a974-dbcc34c97892 | -5.82609 | -53.85982 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19320f71-d904-3000-92d2-b398d30e745d | -4.46013 | -54.97057 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 75541cae-c6ef-3b98-b18d-d606da142267 | -6.44621 | -55.43964 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9feba491-6a1d-3033-a80e-21b746a3180b | -6.89585 | -43.67984 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fce1dda7-bfd3-3b7d-8848-13e03bb637ea | -3.70795 | -58.92952 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a16dd4e-e161-35ce-aaba-49e9beb98488 | -10.97085 | -45.41647 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e03814c-6452-3b77-81f5-9303b0c16838 | -11.34978 | -46.65404 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ab4acb6-47c4-32d4-a150-7b5a1e26ad2e | -5.68278 | -53.49626 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2a93bfc-1114-375d-b76a-1418c4796b35 | -11.27706 | -45.51577 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| fbacc538-6ae9-37cc-9ba1-e17c26369e19 | -10.50005 | -44.41723 | 2026-10-06 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
