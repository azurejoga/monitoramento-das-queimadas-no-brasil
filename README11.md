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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d118129-2bb3-3a69-9dfe-0253383961ed | -13.64928 | -48.99781 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 447f99d3-5a1f-3cc7-b8d2-94680a42e130 | -7.61318 | -45.19695 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c964eed9-2fbe-31cf-b951-d1ed8e0c89ac | -12.24427 | -45.05567 | 2025-08-11 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0854c7ae-5f91-3b61-8e31-417aece92e74 | -11.696 | -50.12616 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3a3bac8-a9c5-3dbd-b8a1-d3d2435c70f4 | -9.2117 | -44.52816 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6901464-0ac8-32cd-ada9-c522877dec10 | -9.15664 | -44.42107 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89934c5c-cb37-3b03-9a1a-38130a784c6f | -9.86625 | -43.54407 | 2025-08-11 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d004f2a9-07b2-316e-af9e-44ac4ae0ac4b | -13.6146 | -46.92662 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5832155c-bfbb-3bbd-8adc-e0944539e9d3 | -11.71533 | -50.10676 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae39258-7ef8-34d4-82ad-727e16c3a742 | -7.65653 | -43.84069 | 2025-08-11 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3fb9ee5-7786-3332-b10a-22e0676a9708 | -8.57308 | -54.67735 | 2025-08-11 04:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73b72bf5-cf95-31de-a659-c1af46562097 | -7.62249 | -45.19111 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7915d9f2-b102-3ecf-8f7f-0c5b5e97a7fc | -11.77744 | -47.39124 | 2025-08-11 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a76b67e-cc86-3975-8780-4eccbc8b7f40 | -11.05002 | -43.27085 | 2025-08-11 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ffc52ad-0ab9-39f8-b094-b0879559c00e | -11.71539 | -50.10975 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e31b5066-f360-332e-9f2b-465373c41bb5 | -10.3685 | -50.82809 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6dc8f6f-e85f-328f-8351-e33e755e0860 | -14.67862 | -42.51402 | 2025-08-11 04:04:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8987ce8b-f173-3f82-a427-5ba8e8f1f666 | -14.11667 | -45.40107 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1533f098-0590-3402-a76d-d30ce8c5f3c0 | -10.30479 | -48.11008 | 2025-08-11 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0032c49-9c12-32cd-aa38-d5dc396379d9 | -14.11294 | -45.40039 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d478584f-b313-32f3-a238-d4f298d792a2 | -11.77878 | -49.57085 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d0b129f-e044-35d4-be18-b49e82e879c5 | -14.08559 | -46.57952 | 2025-08-11 04:04:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0a50409-a07c-30c2-bafe-78c4b3484a0a | -12.40127 | -40.9132 | 2025-08-11 04:04:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 781e3545-6d14-310a-9c6a-a2f17c95004a | -7.87558 | -44.96883 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 767b7781-e067-3ad7-a860-c557af45df33 | -10.36363 | -50.82299 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eef72d66-1e19-3822-8419-fd58804644f9 | -13.59138 | -46.94863 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbbb42d2-fd5f-335b-b413-f853699099c8 | -12.57855 | -41.27088 | 2025-08-11 04:04:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5dd8d5a-207f-35a0-8a5a-c32c204761a1 | -11.92905 | -49.55889 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01afb05a-a21c-37c4-b349-9a6d6ef07826 | -14.0141 | -42.53991 | 2025-08-11 04:04:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5829ce2f-b497-36ed-8d97-eb28a7028edb | -13.59195 | -46.94538 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fe5e81f-e5b7-354b-b3b7-e34729afc7de | -7.26036 | -45.37041 | 2025-08-11 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbd1e924-3895-3be0-9d46-388ac169489a | -13.64635 | -48.9936 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95eb2f21-bbec-34b7-ab80-703f4f7cb2a9 | -10.42328 | -46.25327 | 2025-08-11 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c16896e9-8f10-3d57-ac34-bf4a90d5d7bc | -13.6139 | -46.93043 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb92ff76-2644-3316-89b9-496ceb90dacc | -14.11393 | -44.87813 | 2025-08-11 04:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2bbde8a-c0f9-3d11-8564-2ca5675e98b4 | -11.65995 | -42.85444 | 2025-08-11 04:04:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ab02093-737f-38ee-b57f-8e468c87be48 | -14.1196 | -45.40631 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c89ff376-fad0-3ef3-aedc-89e5f58bc85c | -11.39778 | -50.59624 | 2025-08-11 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60ac78eb-3edc-37e9-b1f4-99aa84a848e2 | -11.39235 | -50.59513 | 2025-08-11 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d1d3aca-d20e-31c5-bb77-ce399387921c | -13.59081 | -46.9518 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 396bba2c-290f-34c9-9b0e-92f8ba1e6ae2 | -7.21704 | -46.24629 | 2025-08-11 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96e1847b-f078-36a1-b774-d48d9d2f4f4e | -11.77936 | -49.56774 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ce477a1-50ac-3bcb-af85-e9c532b8c53a | -10.36993 | -50.8205 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25f0332f-2c1b-328e-b060-07e5a0a23574 | -12.57744 | -41.27794 | 2025-08-11 04:04:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7af103de-067a-39ef-b17e-ad1d7258c3f0 | -11.76104 | -49.11575 | 2025-08-11 04:04:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a53f8ffb-3a49-32a1-b426-67378185d1ef | -12.1385 | -45.03912 | 2025-08-11 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99905569-e5e4-347d-95f6-ea4669653ed6 | -9.86556 | -43.54817 | 2025-08-11 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 726e172e-1c16-3a1b-b2df-ae313404558e | -7.21774 | -46.24213 | 2025-08-11 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd53f62a-501c-3c9e-b39b-ada9be176ffa | -9.21628 | -44.52417 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80f8f638-03db-3674-8dc2-8e1862d0b2b1 | -9.21484 | -48.53629 | 2025-08-11 04:04:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3439dceb-7ddd-303a-8e3f-8184e1c82b7c | -11.95123 | -43.39339 | 2025-08-11 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7bbea317-65b0-3345-88b4-ad5425a6060f | -10.4198 | -46.24872 | 2025-08-11 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dd3ae85-3ced-354f-86eb-f4b81eb0d878 | -7.43044 | -43.76059 | 2025-08-11 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 904d918b-67b8-3880-8e76-114d424118d5 | -12.65236 | -44.37474 | 2025-08-11 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f3eddee-e109-3bad-b2cd-baf3da9085ea | -14.11375 | -45.39584 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f34127c-334d-3bf1-8dff-f5492a66518a | -11.39842 | -50.59626 | 2025-08-11 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 461b395a-ec47-314e-b27e-c6f861716293 | -11.39298 | -50.59517 | 2025-08-11 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dadcead-6fde-3bf9-ba45-8c79806e35a1 | -9.64596 | -43.83116 | 2025-08-11 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 73667e29-8033-3f7f-a57c-e75b533a439f | -10.46208 | -44.39008 | 2025-08-11 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc846817-35ab-3ad1-aadb-7687fb6e94c3 | -11.94427 | -43.39223 | 2025-08-11 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24484718-718b-3780-b163-a0992ced9df1 | -11.7783 | -47.55984 | 2025-08-11 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb2f826f-3873-362e-a59b-42cdf2f550bc | -8.30319 | -44.98905 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48b23c18-a134-3717-ae4b-9168c018e47d | -7.35285 | -44.59382 | 2025-08-11 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0f61fb1-44fc-3f55-a5f7-62337de05fe4 | -7.8732 | -44.97029 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 719b465c-fea9-32af-bdb4-395e037920bb | -12.40736 | -41.15289 | 2025-08-11 04:04:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f03b2cc1-83c0-3a80-b44c-d685f7991322 | -9.2079 | -44.52753 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd223321-ad04-3f9d-bb09-197e4f05a5ca | -13.62157 | -46.93502 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc32b686-39c3-3bdb-952b-945430d01c60 | -13.59256 | -46.94199 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1b16fc5-0182-3732-8e8b-7bb5bdf5986f | -11.36546 | -41.59477 | 2025-08-11 04:04:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d5603b1f-7679-321f-a03a-58622b770c9b | -8.30518 | -44.98664 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90cb9291-1cce-3d96-9b52-ba718f7e1b6f | -13.64472 | -48.99603 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7428ca8d-78f4-3d17-a033-fc92ff5d61f0 | -14.48028 | -47.07678 | 2025-08-11 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e100da6-94ca-3763-8b8a-b5c41b32712e | -11.06481 | -43.18121 | 2025-08-11 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a68c0a4-3a78-34e4-bcc0-0e66a8ce0ec1 | -12.35775 | -44.43652 | 2025-08-11 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d4f0ef4-7bba-3c87-8cad-84e08325ff97 | -11.77994 | -49.56463 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1430ccdc-72ec-3a39-a2d2-7534770d0414 | -14.1204 | -45.40175 | 2025-08-11 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63bfe1fc-abff-302b-a0f2-33a436b03d4a | -9.2274 | -48.52865 | 2025-08-11 04:04:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 411bc029-a041-3272-ab4b-aad536d94ec3 | -7.35428 | -45.27663 | 2025-08-11 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 219c86ba-00f7-320c-8af0-32953ba22f03 | -14.12337 | -44.86667 | 2025-08-11 04:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14179c1c-50cf-3d47-9b16-29bc59fa4c17 | -13.59316 | -46.93857 | 2025-08-11 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06b2ab2c-3d43-3454-8bbf-fcfa1c94079f | -8.98867 | -45.69331 | 2025-08-11 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0d0f50a-22e4-3b38-9144-f057c04597a8 | -8.5586 | -54.67415 | 2025-08-11 04:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2621c661-f211-39da-ab5c-0fd0bb1a453a | -13.33962 | -43.37804 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5f3bdcc0-f239-3911-bea6-2cda03bdc857 | -10.4687 | -44.39596 | 2025-08-11 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 436f6cec-9f5d-3889-8c8f-f1dd9ee7f1e3 | -11.93103 | -49.55866 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff0fb182-6d01-3bff-ada2-afb8bc1a8aa7 | -14.57113 | -47.1489 | 2025-08-11 04:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be1ea77e-7002-3779-b86b-d595eba99091 | -13.64543 | -48.99836 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fbac840a-66a0-38d4-bae8-a876081db2c5 | -14.48164 | -47.06931 | 2025-08-11 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 445743a6-cdad-3a80-bbbb-482e2502afe0 | -11.69538 | -50.12943 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 266df2d5-26d5-3a77-9420-be93b7bbf7d6 | -10.37136 | -50.81293 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9506f1b-8af0-3a4e-927a-75539a3b36a2 | -14.57182 | -47.14513 | 2025-08-11 04:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bcc8c77-d62f-37bc-aab2-a91847a21425 | -11.71661 | -50.10323 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75cfa0f7-4d75-3876-b3af-3ba7fa1912ce | -10.36922 | -50.8243 | 2025-08-11 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f12e519-06e1-3e9c-819d-726000aee8b5 | -7.87161 | -44.96814 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e50fa18b-069f-3c87-aa66-686f36820e77 | -11.716 | -50.10649 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea7e37e-3fec-3f3e-b7dc-b314c81c1c72 | -10.62518 | -44.74814 | 2025-08-11 04:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7e90be1-4997-3b04-a5db-501ade306365 | -9.64526 | -43.83536 | 2025-08-11 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39fd0924-78f9-3d89-899b-f793f2af9e34 | -11.70946 | -50.10897 | 2025-08-11 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 314faf0d-450c-38b6-a5f9-0513eacd7a16 | -14.12263 | -44.87097 | 2025-08-11 04:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2923c5c9-6a7a-35f0-8664-dfcfe2e537cf | -12.04467 | -45.76587 | 2025-08-11 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
