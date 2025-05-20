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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aeb0edc7-77d0-3725-afda-bf356e78a242 | -8.19978 | -49.6912 | 2025-05-20 04:32:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dafe912-3880-3148-b67f-6a4ba3ec0f62 | -6.1639 | -44.00685 | 2025-05-20 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b5bd4ef-0a14-37d0-904d-44a28778d420 | -7.07405 | -44.91493 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f4b7231-8106-3354-868d-4b1d5b5ae965 | -6.23254 | -43.35151 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b669682b-af7f-3c7e-aa19-369b918f0ae2 | -7.0704 | -44.92455 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fefcb6c6-e17e-3027-921e-98b557515dd5 | -5.97207 | -43.75879 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1e56bad-0f66-38b1-9f4b-6f753650d653 | -7.06925 | -44.92263 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a3368ea-8cd5-3872-bd5e-12555ffce4a8 | -6.83392 | -45.3631 | 2025-05-20 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68d44004-0564-3f77-82cc-8dcfc4b0cfb9 | -6.23642 | -43.35205 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 93e5592e-7e48-397e-9dbc-e8d6a32c34c9 | -5.97653 | -43.75471 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 53bdbcdf-918f-3a0b-a478-8b2bb7948df3 | -5.76801 | -43.49232 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5db434c-38c8-3249-81db-6150e0c0ab47 | -7.37343 | -49.58149 | 2025-05-20 04:32:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d723697b-7940-36a5-9df9-419536a19978 | -7.07166 | -44.91629 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97e405ee-cd53-38ea-b45d-7db0bc239303 | -7.07344 | -44.91908 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69c71d61-379a-3afc-adf0-3508d984290d | -9.43756 | -40.37782 | 2025-05-20 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 76966ad6-cfb0-3554-82bd-2bee8aa19efc | -7.06745 | -44.91984 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74d56f00-36fa-31f2-b7a4-3af708d1ae80 | -5.76038 | -43.49108 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72eb9b54-cf97-3d5a-88cd-e732752fd161 | -7.07283 | -44.92321 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6bc83fe-7526-3c06-a312-86a9d1057464 | -5.97516 | -43.764 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcb35c02-c3b0-3006-972a-28644496d647 | -7.0645 | -44.91509 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a842dee0-bdfd-3cf7-9c22-6b3b926bdaa0 | -5.7675 | -43.48913 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf60fe2-0771-3f09-8a61-162733f74241 | -7.0662 | -44.92806 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb47116b-625e-3ca6-9064-750e01b339b3 | -3.08258 | -40.07722 | 2025-05-20 04:32:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a13f9c30-2234-3a01-817b-404af0b9f2ba | -7.43467 | -46.69238 | 2025-05-20 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eccaeb4-a94d-3591-9f37-2ff5bda21d60 | -5.54333 | -47.46178 | 2025-05-20 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65e9f920-69af-3758-9b50-b1fcf3941937 | -9.44163 | -40.3785 | 2025-05-20 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b4f91240-a983-3caa-bc07-517c0bcd953e | -7.07524 | -44.91686 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2315954e-8b27-3f6c-80d3-5020f6fa8725 | -7.07103 | -44.92042 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7f47420-24c3-39e3-9162-b4bd00c8cbfb | -5.75986 | -43.48787 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7859a555-c9e4-3379-a609-4a09ceac37f9 | -6.23326 | -43.34649 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfc51c05-e514-37a0-878e-c0a2977f295b | -7.31074 | -55.30677 | 2025-05-20 04:32:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2fbe501-48ac-3cfd-a411-0a5d70dfe0d9 | -6.22793 | -43.3559 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 827351c2-6cf6-3e91-86bd-969f00301fa8 | -7.06558 | -44.93211 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a349da05-06f3-383d-a3bb-629548594519 | -7.07046 | -44.91435 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 369104d9-6931-3830-b1f6-12a741d109cb | -8.07146 | -47.12602 | 2025-05-20 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 881a1286-b34a-3e77-ad1f-465c14064b8d | -5.96451 | -43.75769 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b29d7562-18ff-305e-9695-49be7c3cba47 | -6.32201 | -43.7486 | 2025-05-20 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f535f3c4-8324-3dc5-9371-282d412f6f84 | -7.06865 | -44.92675 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92c4bf8c-1d0a-3081-afc8-9109885f7256 | -6.21127 | -43.32566 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b14f51e-e530-3705-8429-a2f9cc6302a1 | -5.87903 | -43.93845 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efc467a8-9935-3de6-9652-b5f0004dfa3c | -3.42237 | -43.16338 | 2025-05-20 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 995418b5-8eb3-39f6-a334-a051b65ecd5a | -7.67484 | -48.06044 | 2025-05-20 04:32:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c85b762b-38b6-3023-a7c0-8e89bff6c98d | -12.27415 | -57.26487 | 2025-05-20 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce4ef36d-2708-3060-980c-f2576f5b26ef | -11.41929 | -44.70234 | 2025-05-20 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ca3e687-86bc-3c9e-bf57-5a112d38e3d6 | -13.04543 | -53.71743 | 2025-05-20 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4becc552-4801-3b81-9515-9bda88041a3e | -11.69507 | -47.79257 | 2025-05-20 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e36e186-6422-35c8-b46d-3edf9f93fdbd | -12.08273 | -54.58176 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 186c5ce5-ad05-3b7f-992b-384f0a4eb744 | -14.02776 | -55.14251 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eaee5b9c-5754-38e4-afd0-5c491ea93d0a | -10.35855 | -47.97482 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b932e33a-1771-3b90-8580-74945779c8d3 | -13.31924 | -45.37437 | 2025-05-20 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fb3d152-7fe3-3457-9bc3-b07e56be35ed | -14.82916 | -48.43012 | 2025-05-20 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 664fadfa-9144-31a8-977a-b7a01f69edff | -12.42947 | -43.72917 | 2025-05-20 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a90aad6c-0e16-30f6-9552-31a8c06bbb96 | -12.07137 | -47.32005 | 2025-05-20 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b8e745a-80fd-3f14-8ddd-389b10a06d64 | -13.15181 | -44.93147 | 2025-05-20 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14affdfa-bc94-3d57-bc77-c048814b144e | -11.51576 | -48.58357 | 2025-05-20 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be982e68-7ab4-3547-8328-c72c5fb23fe6 | -10.61397 | -46.98658 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b00311b-d31c-30ac-92b3-4a67a1b1e3fd | -11.00743 | -50.75832 | 2025-05-20 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11ff5c4e-7d96-36fb-995e-b2c5a2823216 | -15.38783 | -47.96801 | 2025-05-20 04:34:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87df1cb2-8fb1-3976-b11d-dd73b849a2a5 | -12.83733 | -47.40049 | 2025-05-20 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b7c5e69-aeac-355a-a3dd-b8879050b655 | -11.23484 | -49.48866 | 2025-05-20 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6281171e-ff4d-3cf4-80fa-b57dd6199fea | -10.36519 | -47.97588 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28356d6e-bc9f-3152-82d5-137c05e12e0e | -11.32353 | -57.84441 | 2025-05-20 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f394137-8acd-3612-9661-893cc61bace8 | -14.03595 | -55.12085 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13a29527-7fe9-3ba6-b573-ef4c79bdbb71 | -10.07816 | -55.493 | 2025-05-20 04:34:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9de7aee-350b-39d3-976b-3ce51b4ffa45 | -14.0457 | -56.07288 | 2025-05-20 04:34:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5343682e-b0ff-3b2a-9485-fb88017525ea | -9.03407 | -48.94181 | 2025-05-20 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32f63fef-9b11-362a-a399-bffc52a3c3cf | -13.04461 | -53.72224 | 2025-05-20 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 843e4a6d-b0f3-3977-9424-4abe60290c99 | -8.63624 | -51.28804 | 2025-05-20 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c46f451d-76f1-3b43-971a-f5ff237f4014 | -8.63269 | -51.28748 | 2025-05-20 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43f58b3f-08af-3867-a548-db2f460a8638 | -12.06797 | -47.31951 | 2025-05-20 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccd65d4d-c52c-318f-89ae-80183cc995de | -12.43466 | -43.72216 | 2025-05-20 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a681b6ee-f8a0-33d6-b5cf-a6c9bb4afa12 | -13.6659 | -53.93419 | 2025-05-20 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a97e372-a2c0-3300-a396-0ee2303c8c3e | -13.02459 | -45.0716 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37f5089a-abe9-3367-9080-56e294922581 | -11.66596 | -54.93942 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fc8885d-83e6-33d9-8af8-9f8eb3877664 | -10.76691 | -54.77817 | 2025-05-20 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b01235ee-226f-3f76-838b-c21a8ed4fbd6 | -11.36317 | -55.12444 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4fc8a9a-733c-3f6f-af3b-9806a922c556 | -12.27901 | -57.26579 | 2025-05-20 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 151b32a0-7f19-3dd0-91be-dba8fecd78d8 | -12.11755 | -47.98748 | 2025-05-20 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd4161b4-f615-349e-90ab-a83f5fd8e13f | -8.74615 | -49.74614 | 2025-05-20 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 524e25c0-b805-318d-98be-7b8d73a9a3a9 | -13.57818 | -47.36459 | 2025-05-20 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bb15bc9-57e5-3bfc-8cc4-1cd4daeb2e39 | -12.27798 | -57.27135 | 2025-05-20 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 056f069d-0e53-307e-a185-733bb77f87eb | -14.03391 | -55.13203 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8043f777-0ec2-3ad5-a785-2744652cbe79 | -12.98752 | -46.32442 | 2025-05-20 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 159a9add-dfda-3145-9f0b-c5fe1fc3f783 | -13.31611 | -45.36911 | 2025-05-20 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7328fd3-9538-309c-9612-f3cf596c23ea | -8.70066 | -49.02758 | 2025-05-20 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97579b5b-e79a-3b6c-a455-b31916622165 | -9.04226 | -47.75695 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbbc148b-e5a1-3e9a-aae8-bfe5e02e1662 | -14.02413 | -55.12193 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01eebc8c-d788-3e6e-8851-6657664f6772 | -10.76012 | -57.23037 | 2025-05-20 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d4d76e-dc61-3c9e-b420-725f9bf43c1a | -10.36187 | -47.97535 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0511aa8-07ba-3528-8a22-b5d20761f08d | -10.61057 | -46.98603 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 741b2136-aa14-3f96-8642-fa9228f0f35e | -11.34824 | -55.10897 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd7d34c-5550-3aa7-8d26-8250bc950821 | -14.01981 | -53.02977 | 2025-05-20 04:34:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61aaed02-916d-3e4d-87a7-02f52a130ae1 | -8.7517 | -49.7544 | 2025-05-20 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f97bccb-b971-3fc0-b940-8c7a39863766 | -11.36391 | -55.1203 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c1623b-81ce-3ff2-9a05-defbe3bb45f4 | -12.04023 | -54.96507 | 2025-05-20 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 598f6dd3-3b0f-360a-a043-98ffcce3f607 | -15.27249 | -43.07688 | 2025-05-20 04:34:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d18fd825-8e33-3654-9f65-b600af68c37a | -13.71193 | -57.48006 | 2025-05-20 04:34:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| caba96d7-0ec6-385c-98f7-009a7c13a000 | -11.15256 | -56.78651 | 2025-05-20 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1399471c-1787-324c-a198-84667a1007cd | -14.01955 | -55.14101 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a70eab4-3ada-31c5-a89b-4f740754941f | -10.81989 | -56.96053 | 2025-05-20 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README7.md)
