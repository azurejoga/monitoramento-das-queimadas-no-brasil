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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4d19253-4ad2-360c-bdc5-bba59f810054 | -11.81473 | -47.50845 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d27cb093-d048-3ad9-80ac-41a6805d11ef | -11.55658 | -47.09018 | 2025-07-20 04:17:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2815f76c-07cb-3284-8d25-27688b21c028 | -11.28077 | -40.98092 | 2025-07-20 04:17:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ca03a5d-6ec6-35ab-a9f9-aec2a9bd36c1 | -11.48628 | -47.32636 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f64c34c-1ad7-3243-95a7-a6c5c5b202dd | -8.08421 | -50.11157 | 2025-07-20 04:17:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 855abf74-4efc-32f4-a10b-4748100b1e40 | -10.66997 | -49.67879 | 2025-07-20 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76a4df9d-18a3-36aa-81e8-5c7a673d3b94 | -10.68285 | -46.78738 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aaa646f5-6504-3cd8-9bb5-afc5bf740fe6 | -7.99449 | -43.68377 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebafead9-7b0b-3757-9f4c-c8884cf55e20 | -6.86237 | -47.81776 | 2025-07-20 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 198f5813-7433-314c-bb08-a643484b8565 | -9.47276 | -57.83279 | 2025-07-20 04:17:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2070157d-1deb-3b91-a44e-a034396a32bc | -10.66314 | -46.79646 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 508be687-c306-3981-9d18-791f455ff748 | -7.70212 | -47.29379 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 747d41af-4851-35b9-a2da-3e5b92a5ec17 | -10.87398 | -47.17114 | 2025-07-20 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 150d07da-cd9a-320a-ae45-0ea17694a412 | -11.95646 | -46.75331 | 2025-07-20 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ad70852-505b-334b-8b11-a8c70dcf2224 | -7.74666 | -42.16235 | 2025-07-20 04:17:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| efeb51cf-aa1c-3085-8482-414541a4aece | -7.99504 | -43.6803 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26cbf528-3e89-3f46-8894-8124de51eaaa | -10.65404 | -46.80737 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9947f409-d749-329a-9d6c-adb75b1d4193 | -7.29199 | -43.88574 | 2025-07-20 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34ef5ebd-a43e-3e54-8563-520837e071a6 | -8.07679 | -50.10081 | 2025-07-20 04:17:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8786f8f-24d9-3b97-8192-7518a5f4cd27 | -7.42564 | -44.28629 | 2025-07-20 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed568be9-b6a2-3cc9-8505-47a9a82c30cc | -8.45583 | -46.03254 | 2025-07-20 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dd83c9c-5350-33d8-84fe-5f5c7863ebe5 | -10.65049 | -46.80679 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6bf6b7f4-bc7e-34ef-b875-6beef0063e76 | -5.08901 | -48.42302 | 2025-07-20 04:17:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b44d5be6-809c-30cb-9694-8a9db048c10e | -8.0887 | -50.11237 | 2025-07-20 04:17:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6c2590b-f86e-3639-8cc7-5ffa6ce040d3 | -10.62457 | -44.76572 | 2025-07-20 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a92c321-050e-331b-a71c-504b26d7f7ec | -10.66735 | -46.79304 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4e1d18b-6ea4-34a9-807a-575d6e070813 | -11.4624 | -48.16407 | 2025-07-20 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 783c0d01-d9fa-307e-a1df-233303c5a95d | -7.69776 | -47.29639 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e70a2ea5-8615-39e6-b7c5-dbf423e1fadc | -11.8133 | -47.51682 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bd83c09-d407-3a1a-985b-233d6c6e0995 | -11.48435 | -47.3202 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bac9b081-e4ad-379c-b785-006766f19663 | -11.46616 | -48.16478 | 2025-07-20 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65d4c5c6-6032-323f-b8c3-194dcef5637e | -7.70664 | -47.28982 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 29bde480-0fb1-3b79-b78d-b9432912e6e6 | -11.48723 | -47.325 | 2025-07-20 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fa7624a-c634-3da0-b785-50909fe87053 | -10.6832 | -49.67717 | 2025-07-20 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b26c38d-e3d6-3686-8b87-ccaf80b53776 | -7.33358 | -43.04792 | 2025-07-20 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b1c3c7e-c191-30c8-bfdc-72787494767c | -10.72696 | -52.51788 | 2025-07-20 04:17:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e04bf7e6-43be-315e-a052-975ae3431fa3 | -8.35668 | -46.6474 | 2025-07-20 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560dbb64-d5e2-36d5-a199-d62a5022cb7c | -9.91222 | -55.52897 | 2025-07-20 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 856aec97-9a0b-3b31-b58c-f234f9690ccd | -5.34888 | -45.26876 | 2025-07-20 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9970d617-1145-3d36-a04f-df6685f6a5a3 | -10.70121 | -46.78641 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8db39c7-ec8e-3b44-89e8-0616d4d45fac | -11.83393 | -48.20802 | 2025-07-20 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f117e989-0826-3f4e-b26b-357f9d1ef745 | -5.42507 | -44.0011 | 2025-07-20 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 214360bb-8889-3ad7-8116-79cee2c3a44c | -9.59569 | -43.85397 | 2025-07-20 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d907906b-6d54-34d2-a0aa-b133a28bf559 | -6.6336 | -48.08342 | 2025-07-20 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8ef6800-cd58-3771-b256-49ac7d6a4ca7 | -11.82196 | -47.50971 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3cfd3f0-8681-3f30-8dc6-21dd23e6a0c9 | -10.67902 | -49.67642 | 2025-07-20 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c75e0dd-26ca-3612-9031-d49f6ebd6de4 | -7.69834 | -47.29317 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e28bdf1f-f94e-3e4f-8868-d08f5a167db2 | -9.53921 | -40.33427 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| df081712-a463-3f1a-8c35-9f7e3489ffc5 | -8.3603 | -46.64796 | 2025-07-20 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59fa9821-57b5-3272-8206-90574c4e4272 | -10.62811 | -45.23521 | 2025-07-20 04:17:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be5ba83-700f-32b1-b5a3-6902868fd6db | -7.99339 | -43.69073 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2620e72e-b222-3ac6-b80a-fb62630f4dde | -8.04885 | -42.14955 | 2025-07-20 04:17:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 834054f9-bb7b-371c-8104-0769502d7a3f | -10.66602 | -46.80106 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 40fcc272-c6e0-32f7-9b89-39870d2ec88b | -11.83495 | -47.49895 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 627c9c5e-5ea2-392e-a780-7dc99c9d5a89 | -12.70937 | -45.027 | 2025-07-20 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7da9d319-1a94-3033-ac4c-356430b94fa2 | -7.70985 | -47.29372 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 067798a4-8701-318d-808a-35a3e7ca38e8 | -7.42285 | -44.28226 | 2025-07-20 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73c81994-00ca-3d59-8fc9-caa4e6630f8a | -8.63738 | -49.42488 | 2025-07-20 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15d9bf8f-eb77-3166-8e03-cd803c16cc4a | -11.5763 | -47.85818 | 2025-07-20 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc6399c0-1f7b-3d4f-adbd-f6900e820a7a | -5.49838 | -44.34648 | 2025-07-20 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d706af75-8409-3fc4-aecd-3811167ea0bb | -9.10894 | -45.94633 | 2025-07-20 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da81a743-c08b-3789-984a-c4e360d79b8e | -11.56014 | -47.09078 | 2025-07-20 04:17:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95fed92a-b169-3cee-a09a-fa2288335377 | -8.26094 | -46.36291 | 2025-07-20 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a2b9cba-0751-39ec-b238-8ec7476b5364 | -11.49703 | -48.07572 | 2025-07-20 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14a6df9e-8428-3292-b2d3-17870dba9859 | -11.83768 | -48.20868 | 2025-07-20 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e33f19c-5afd-3358-a11b-612e2d7f1866 | -7.76123 | -42.1573 | 2025-07-20 04:17:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a0dddab-7ceb-3fad-ab59-35b4aae706ca | -11.49329 | -48.07507 | 2025-07-20 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0675086c-4296-3631-bc59-29dfbf247f9a | -12.3632 | -46.43089 | 2025-07-20 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e1da4c4-a63a-3221-91f8-a9ad40c131d7 | -10.6906 | -46.78458 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0d5d00f2-d0a7-3db6-ab9e-9fa1f20986c1 | -7.47626 | -49.45498 | 2025-07-20 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a648d15-c78e-337d-a6fe-4c1ea954087d | -10.67023 | -46.79764 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0f289007-990f-3f41-b880-6aa49867d9ff | -12.05766 | -41.06161 | 2025-07-20 04:17:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d89f3f3-7ad3-3445-b2d9-f8201737c97c | -9.54354 | -40.33048 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.4 |
| ba24d4c0-354d-33a6-924c-6da3967d7115 | -9.53986 | -40.32993 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| f55ded5b-f8e3-3918-b761-1797d5618fb5 | -6.81103 | -43.80568 | 2025-07-20 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0722d61-8c80-3d22-8437-4b0bf49851ad | -8.04492 | -42.15261 | 2025-07-20 04:17:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf804735-f367-3dc8-9259-5040cea2a017 | -7.69932 | -47.28719 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ef31a3a-57c2-3286-b5ea-b4e65e335146 | -10.67443 | -46.79425 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1fb0b359-2f75-375f-a591-d5f64da51d7b | -7.7053 | -47.29768 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efa81547-5043-366f-8dbe-e560a4713034 | -10.68993 | -46.78859 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 96520496-8f1e-35fc-b4bb-b1c2ccd7ef92 | -7.29208 | -48.32295 | 2025-07-20 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9ea1168-555e-394f-be4c-14d8d69e1fbb | -9.11304 | -48.12114 | 2025-07-20 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0c61121-0227-3d7f-baa6-105d85032cc7 | -10.69237 | -46.81804 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25bd3bd5-c53e-3c4a-a8b6-587fada25bf1 | -5.80316 | -43.92611 | 2025-07-20 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed42314e-24e0-37ae-9598-66dc692fac58 | -10.67864 | -46.79082 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c2ecba4b-b711-364e-a36b-4ca96fce978c | -10.627 | -48.09234 | 2025-07-20 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ce734ce-ef0b-30d7-8201-51a0244bb9e3 | -10.63541 | -45.23273 | 2025-07-20 04:17:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1652fe03-1f98-3705-b6ce-5411ff5cfeaa | -7.99726 | -43.68778 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2a9a6d2-0985-3f7a-8747-e00203e5700a | -6.7482 | -44.19963 | 2025-07-20 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1664ad7-494e-3154-8d75-74195ebf45e9 | -10.73257 | -52.51582 | 2025-07-20 04:17:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65df586f-5c42-3c88-b3a3-69c4e01e3241 | -7.99671 | -43.69126 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18527432-1055-3dfb-9905-1000d8c6d91b | -7.29385 | -39.6291 | 2025-07-20 04:17:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d280a2d4-28e4-3bb6-a1a5-f784fce5cf12 | -17.8836 | -51.68484 | 2025-07-20 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0fa154e-5350-3ff4-bc9e-9d5bab90fe22 | -16.70781 | -49.35958 | 2025-07-20 04:17:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a24f3344-2fe0-3ea2-a192-ff51b77aa8ec | -15.99402 | -49.82163 | 2025-07-20 04:17:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 051a10b9-2c97-388b-b204-00370b2179cb | -16.77957 | -49.32734 | 2025-07-20 04:17:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3db02ef8-e2ec-31b8-b7de-bb69738853b8 | -14.20653 | -54.65353 | 2025-07-20 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00be398b-e8a4-3726-b484-c66ef0ce1a39 | -14.79111 | -48.29517 | 2025-07-20 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bc790d0-edc6-3270-b175-733eb2442260 | -16.77931 | -49.32511 | 2025-07-20 04:17:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3d084f1-a5c7-3ef5-9275-ae0980dcacd2 | -16.08651 | -45.17234 | 2025-07-20 04:17:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
