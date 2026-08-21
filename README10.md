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
| 24f476f6-f942-3763-81a1-236f13eba600 | -12.2603 | -43.154999 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 40d9e302-b93e-3439-b7df-ab1a934ac8ca | -20.956499 | -49.134701 | 2026-08-21 00:42:00 | METOP-C | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4abb9eba-c49a-386c-96a5-29ce8cccefd1 | -10.732 | -44.789902 | 2026-08-21 00:42:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06eebe06-6eb9-33f3-b6d5-3abd70c35012 | -11.6396 | -46.541 | 2026-08-21 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd467ab-3345-3abd-b290-d9bd663c5212 | -8.5729 | -54.6688 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e5d175-6d0c-339a-a840-206b496df465 | -6.5858 | -58.9814 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea2b3252-dd5e-32e8-84b4-b4d8b82ae98d | -11.3819 | -50.719299 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1ea4b9-1953-3e89-afad-11cb5b1aa0cd | -13.3928 | -54.387199 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82ade342-5157-39dc-ae75-a88d68660328 | -13.4514 | -51.774101 | 2026-08-21 00:42:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7f163e4-32a7-345e-945e-83e00a33812e | -4.9565 | -56.275501 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44db3f54-8fdc-352c-9105-c6ad9442d816 | -10.2618 | -50.296799 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c57b55f2-5f0d-3f33-872d-2fbecd93d787 | -9.4574 | -51.641499 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16f92075-0e93-3a34-965a-dc903cbc8ed6 | -19.9158 | -44.585602 | 2026-08-21 00:42:00 | METOP-C | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bb049a5-b261-3b29-a493-e332256d04e1 | -9.436 | -51.637699 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3653cbe1-4e82-3633-b69c-5bd2d825ff37 | -8.6532 | -54.614799 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c364c90-a374-3160-bcac-7708378b8769 | -14.7272 | -47.138802 | 2026-08-21 00:42:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fbe63d6f-c2cf-30a8-9411-0c286cd242d6 | -6.3819 | -54.936501 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dfa011e-44fe-366d-bd7a-59692228da37 | -10.7683 | -50.309502 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f382d507-95c8-3399-bfa7-abe79404b546 | -14.3447 | -51.892601 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97bcd9da-eda0-310d-be1a-05becd0f71fc | -21.0853 | -43.2547 | 2026-08-21 00:42:00 | METOP-C | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71822379-ce5e-3695-8b6d-9aa47dc92e60 | -3.5362 | -48.1814 | 2026-08-21 00:42:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f352a26-43c6-30da-813e-cb4912697566 | -9.4458 | -51.635502 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2d5ee6-efe5-3c5e-a280-7fb0e5822dd8 | -8.5459 | -55.312199 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0be1cff-340f-3852-ad31-14b946b65e0b | -3.5379 | -48.188599 | 2026-08-21 00:42:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e786f585-a883-3c01-a175-73769b29bed0 | -10.7439 | -50.338402 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39770fd2-e738-3aa4-abd2-f24611cd77ed | -21.0735 | -43.248901 | 2026-08-21 00:42:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a90d3713-a74d-3e20-8800-8448674e1cec | -6.4377 | -52.759998 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f49d742-361d-3abc-abfa-55564ba8086c | -6.5715 | -58.961498 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 976ae374-2656-3f6a-b0ac-f1c36d695d30 | -11.1678 | -54.004101 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6c524cd-1abb-32b9-9a91-346b6f9f4547 | -18.029699 | -44.608799 | 2026-08-21 00:42:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4e21883-dec8-3c89-82a5-85ccb6269230 | -12.7397 | -48.477001 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8c2f01c-0b46-308d-aeb9-0f6694157c9c | -12.748 | -48.467701 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 550099f9-4f1d-32f6-b237-485c179fa87b | -6.4799 | -43.5495 | 2026-08-21 00:42:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3eca5be8-d666-3d61-a8d2-e8bc69b8fc98 | -10.2919 | -48.223 | 2026-08-21 00:42:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35e4848d-5a4f-34dc-8b46-9e37b8e11c21 | -17.689501 | -44.480499 | 2026-08-21 00:42:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d92893a2-c3eb-3d86-b2f9-7263f723a64c | -12.8526 | -48.4291 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a7b1435-5601-3e5d-ada0-b77e7f35659e | -21.372101 | -44.131401 | 2026-08-21 00:42:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84fc6df7-8788-3b09-a74f-cf46bb9885a9 | -11.488 | -45.1007 | 2026-08-21 00:42:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80ffa6a9-0c19-3620-9194-5a90fd917154 | -10.7201 | -44.783501 | 2026-08-21 00:42:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b79002d-23f6-353c-aa12-5bbf5c850996 | -2.759 | -48.568501 | 2026-08-21 00:42:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33af38a1-b793-39b9-b7b5-d1d523dea987 | -6.2143 | -55.4828 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35593266-4ed7-3b3b-ac17-e9885914b6f6 | -8.0989 | -51.6759 | 2026-08-21 00:42:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2728e019-8bf6-37cd-9ef5-46fe0f728157 | -10.3239 | -50.391998 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37c1abc1-ed13-37ca-a390-f02c9a1aeffc | -12.4316 | -43.390499 | 2026-08-21 00:42:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 520e94da-8e0c-36e5-ba71-1146f61d41de | -6.4302 | -52.725899 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ffd657d-6d71-3030-9ace-8b02e1e8d164 | -14.4632 | -45.625198 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff400b3f-e332-38f5-8dfd-ed14e8f7e79f | -13.4376 | -51.8064 | 2026-08-21 00:42:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa095207-57f0-3f68-9acb-286f6d80d2c7 | -6.3375 | -44.072701 | 2026-08-21 00:42:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5d2ac2a-5523-3124-9e7b-ea614d04df01 | -19.6667 | -46.041801 | 2026-08-21 00:42:00 | METOP-C | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60980823-3524-3162-b668-2d406c322c49 | -10.7357 | -50.348099 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1c1bbd-9abc-3c8d-a718-66668601836a | -20.230801 | -41.480999 | 2026-08-21 00:42:00 | METOP-C | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 100eac00-8fc2-3739-a08f-1c68726efd7c | -11.6618 | -48.355301 | 2026-08-21 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2554f53-4fe2-31ae-b57d-e65c5d79755d | -5.6648 | -51.643799 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d9f221-24ee-3e78-bc73-eb471ba96969 | -13.4026 | -54.3853 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 122918b4-db6b-349d-b5d5-bd15b9e1f654 | -6.8267 | -59.407398 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa22e521-0756-3c06-a2fb-23f674758afd | -6.119 | -57.689999 | 2026-08-21 00:42:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e33d4ff-7aa9-3ec8-b504-496fa8a7781b | -18.7029 | -47.470798 | 2026-08-21 00:42:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8f15c567-0b04-34f6-b71e-3d4897f9f45a | -14.7288 | -47.145802 | 2026-08-21 00:42:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e10296c8-6c07-3d4e-8101-dd4295bf7ab8 | -12.8623 | -48.4268 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29c85578-3fd1-380d-9096-f988e79b376a | -11.6716 | -48.353001 | 2026-08-21 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2476a31c-9af6-3eb3-bd2c-918d04e75075 | -6.2462 | -48.661499 | 2026-08-21 00:42:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21539e7-c10c-33b9-b89e-a0eb74c8b9b9 | -2.4784 | -49.4128 | 2026-08-21 00:42:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa95ccb-92b2-370a-b6db-4c47b0f63de9 | -11.3917 | -50.717201 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9092e157-17cd-39a8-a87b-120497fcdd35 | -14.5717 | -53.009701 | 2026-08-21 00:42:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff2b76f-69bc-3acb-ab12-31f2e122b8af | -7.6364 | -45.760601 | 2026-08-21 00:42:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e34c366-3d67-3184-8ff0-6996e911192a | -3.5346 | -48.174099 | 2026-08-21 00:42:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278e2829-a2f8-3f2d-8d56-928ddc22fc53 | -4.09 | -42.514 | 2026-08-21 00:42:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44d74a52-be2a-306b-a7b7-f9583dc1f247 | -15.1868 | -49.4165 | 2026-08-21 00:42:00 | METOP-C | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9284b6b2-fb7e-3785-a4d0-8d2a1eb4263a | -8.5704 | -54.656898 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0abcb4-b8d9-3fd1-af93-350013e95c65 | -12.0064 | -53.424 | 2026-08-21 00:42:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26897bad-5eaf-3bf8-a020-482a6881af76 | -6.6924 | -58.959599 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b526388-d20f-3f59-9ff1-caa8fd3c7c16 | -10.3141 | -50.394199 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9eb2979-f77c-39df-b50f-df41e1c1a158 | -5.8046 | -55.713699 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5ae014-953e-3f2c-ba2b-6684afe4c071 | -9.0645 | -50.8815 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 941a030a-c50e-3979-8ec2-e72ae4da573c | -20.9582 | -49.143398 | 2026-08-21 00:42:00 | METOP-C | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26de71de-c92c-373d-8db6-1784414ca205 | -6.4771 | -43.5378 | 2026-08-21 00:42:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1fbc203-64ba-33f1-9dce-e06ea0278282 | -20.3134 | -47.216599 | 2026-08-21 00:42:00 | METOP-C | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 76d9fd54-6b40-3ce3-996a-9ded9eecea66 | -12.7495 | -48.474701 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73d2ed16-6c80-3bf2-8843-bae752587b16 | -8.058 | -50.104599 | 2026-08-21 00:42:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb723e0a-ed15-3406-b05d-680b3a4d98fb | -12.8362 | -48.447601 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2452795-12dd-389e-9ab1-2d417387ff16 | -3.5477 | -48.186401 | 2026-08-21 00:42:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbc48fd6-d526-3b0c-8956-81c28b131a48 | -5.6665 | -51.651299 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40a07df4-27ba-3acf-8100-733eaa406db0 | -9.4503 | -51.608898 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c044aa54-fcf9-3edd-9454-4c9895c3dfa0 | -6.8316 | -59.431099 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32ec9052-dccd-3c83-a5f9-554109edcfac | -14.4499 | -45.6124 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcd6122e-e162-328e-a439-7e9e728bc985 | -12.786 | -48.407398 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fff0072-05d3-3af1-a007-6d331c47f979 | -6.3288 | -46.521999 | 2026-08-21 00:42:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c37af52e-c14f-3c51-8ec1-1bd8bbccb8f4 | -14.2994 | -51.8214 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8815b940-7183-38ef-afb9-ce72c36a0b38 | -22.138201 | -46.957699 | 2026-08-21 00:42:00 | METOP-C | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e54e3d28-57ac-38ed-b8c4-0e52ceb594ed | -11.0089 | -45.2159 | 2026-08-21 00:42:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f81804b9-e950-367a-9cca-d4650acaac16 | -18.653999 | -43.178398 | 2026-08-21 00:42:00 | METOP-C | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cba51bed-cec0-343d-88bb-47a871f88848 | -6.8657 | -59.449001 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71cef7f5-6e44-32df-9500-b8b07009e9dd | -10.3108 | -50.2859 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91642dc4-bdb5-31a0-b6b4-2e069129524d | -22.7558 | -41.872601 | 2026-08-21 00:42:00 | METOP-C | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3df75326-f64c-3ef1-bd0d-a98128d47585 | -13.2483 | -51.634602 | 2026-08-21 00:42:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd0c5488-b381-30e2-a79d-1532047a0d75 | -6.4283 | -52.7174 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcc88f7-21ea-3191-acb4-36ef1964d28d | -8.5783 | -54.7425 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89099635-094e-3035-9a3c-4f12e3daaf7a | -6.1645 | -55.441799 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c689b25-d089-3594-ba01-003a667b84f5 | -10.7537 | -50.3363 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bebc579-bc4d-32a0-b449-70c4e125b352 | -6.897 | -55.712002 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
