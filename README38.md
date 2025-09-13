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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f095640f-cb5a-3d00-ae6b-94053f9e2395 | -21.32296 | -44.99114 | 2025-09-13 03:49:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f83148a6-96f3-3142-ad53-9c96b96518bb | -14.43672 | -48.44467 | 2025-09-13 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05f8204d-058b-3a5b-bbad-af58281f87b8 | -20.60293 | -50.40159 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dc43f4d6-1b38-3144-8cf5-f5431362b5c6 | -20.60777 | -50.40811 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4cbe6649-cecf-36d0-8574-7886c9aa7e43 | -16.08242 | -49.95179 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e13208aa-d304-3236-8961-664a70c97f19 | -16.4318 | -49.05538 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2a4b97b-98d4-35e9-83f0-802384e1cc8d | -17.37402 | -41.71207 | 2025-09-13 03:49:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe3d4558-0a2b-3ed2-bed9-4df5a6a5302c | -20.64987 | -48.69354 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ba1f224-a2d2-3657-b63f-f976dbd5b7a4 | -16.05432 | -50.01065 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 97f2513c-4235-3052-8642-c87247bdf061 | -16.84816 | -40.86375 | 2025-09-13 03:49:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 98dccb2a-8ab4-36ec-b86d-8dccec3af2e2 | -17.76908 | -42.17172 | 2025-09-13 03:49:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4f00e6ae-8f65-3977-a58f-18edaee9f164 | -21.58394 | -48.41489 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f6fa2c38-8a32-3a1c-8e7f-8b18ea7a33c9 | -15.85832 | -47.23056 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 740e3675-e38d-3aae-86cd-0d73e7da478d | -21.61778 | -46.81548 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b2964352-0f90-3c66-9fa1-ae073024434a | -15.46785 | -47.32931 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 821273ca-99b0-395b-8590-af5473cedf49 | -16.9772 | -45.81416 | 2025-09-13 03:49:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07fc9dd1-1d58-32e5-8241-c5b8e52e94e8 | -15.60592 | -47.93824 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc7a01fd-11ee-35c9-8d66-6dc26884e256 | -15.14245 | -48.31567 | 2025-09-13 03:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 371c7b8a-92c6-34a5-9d22-af334d3faf5b | -16.06187 | -50.00686 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2b471d57-7124-37f2-8148-23088195e58b | -23.80884 | -50.08783 | 2025-09-13 03:49:00 | NPP-375D | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3414bc69-73f4-32f3-8624-c917e8beca82 | -14.44253 | -47.32106 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22b17aa8-596c-37ac-9c96-65856643e8f5 | -16.78067 | -41.71494 | 2025-09-13 03:49:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 25d74473-08c6-35c6-9ba9-7a0ffac7ed95 | -16.41498 | -49.04548 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d27b4cad-daf8-3233-be01-c848a1ea105e | -17.71275 | -40.26626 | 2025-09-13 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| e68a7e59-47fd-35fb-8f09-5977a5eb57bb | -23.80791 | -50.09177 | 2025-09-13 03:49:00 | NPP-375D | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f27550bf-a73c-373b-966b-43d582050b16 | -15.8335 | -42.60017 | 2025-09-13 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fc3ff560-2fe9-31f2-8aae-c945002fac2d | -15.45989 | -47.33993 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9244e8cf-4b25-3c72-bed2-d0f52d160b78 | -14.45441 | -47.32034 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 914b247c-3f90-3e86-9fc6-723ec599b67a | -16.43285 | -49.05048 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bfe0af77-bba4-3cab-ac0f-374f4b5dc2c6 | -16.36706 | -41.38317 | 2025-09-13 03:49:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d37a2f01-a080-35fb-b430-ea0405e9d2a8 | -16.64986 | -44.92871 | 2025-09-13 03:49:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2732cf22-7792-348a-aa42-3a0d52b06a01 | -21.98211 | -49.9239 | 2025-09-13 03:49:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46806495-594c-3d51-b8ca-ecd626881dd1 | -15.60673 | -47.93446 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 050e4965-5e3c-3a3e-bbf1-6cdf79a022e7 | -23.81065 | -50.08948 | 2025-09-13 03:49:00 | NPP-375D | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2797fade-84ce-375e-b852-d1c120b79722 | -22.65546 | -53.11063 | 2025-09-13 03:49:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5acecc81-7be1-36eb-9a23-cb3e1607fec2 | -16.41722 | -49.24188 | 2025-09-13 03:49:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb10c750-4ebc-3d23-bbeb-3af29760d45a | -16.06624 | -49.99435 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7e78262d-b258-34d0-bece-fec925fe4f8b | -16.08781 | -49.95771 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| be61c1d0-c962-399e-9b24-b23a78688c68 | -16.07812 | -50.00145 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41aa67bb-2d03-34e5-b9b0-6e6ac8b51ce2 | -20.61778 | -50.23015 | 2025-09-13 03:49:00 | NPP-375D | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 291b845d-6d22-377e-8382-5be9682a01c4 | -15.68316 | -49.89764 | 2025-09-13 03:49:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95a2c392-c9cb-34a8-8614-e7c8388fcc7c | -23.61137 | -51.38662 | 2025-09-13 03:49:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5f3e6877-b5b7-341b-aff3-cfe4cd7825ce | -16.28086 | -45.68604 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c7c8ba5-8656-3c3e-a165-7942f8b90b92 | -15.24144 | -51.39489 | 2025-09-13 03:49:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5005facb-b6d0-38cb-8a32-26ced40ee1dc | -15.04863 | -48.16078 | 2025-09-13 03:49:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3820c2a0-d5b8-3909-a4b0-2c6a52b76a64 | -25.515 | -49.10901 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4e15bd70-595a-3980-a831-da9155d70573 | -16.06301 | -50.00155 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e8598747-f9c0-3dd4-a260-9a2010fe9249 | -14.623 | -46.35707 | 2025-09-13 03:49:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa0adbf-123d-3c37-b00b-bbe1953fc479 | -20.60191 | -50.40564 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53cc70a9-84f9-3b0d-90fa-0dd6b16fea9e | -23.14292 | -49.65112 | 2025-09-13 03:49:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| de4af048-de0f-3aaa-acf6-f2431066bf2f | -15.54251 | -47.95097 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de86b579-4f75-3aca-9091-7eaa0c893609 | -15.8342 | -42.5964 | 2025-09-13 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| caae200c-a9e1-3cd7-99db-076d9204dd30 | -15.70411 | -50.58413 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 266b95a8-67c0-38cf-b609-8331498e3afb | -21.31899 | -44.99732 | 2025-09-13 03:49:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 16bc0e0d-bcd5-3eb8-bf95-025cdb45362c | -16.85082 | -41.53802 | 2025-09-13 03:49:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 812d8f84-3375-39ef-bf0e-1b56aa6d87b3 | -22.18712 | -49.61503 | 2025-09-13 03:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72857c95-3b1c-35ca-8280-18cb83ea89e5 | -16.07144 | -50.00124 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b778baa8-fae5-3122-9eba-e77b82e46824 | -16.06901 | -50.01217 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 90bdf31f-e362-3061-99cb-99c0ea32748b | -16.06546 | -49.9902 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1dd940ae-703d-38bc-8895-42534fca1fe6 | -15.68838 | -49.9045 | 2025-09-13 03:49:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0565120d-abf6-3b01-ab3b-cf148b78585a | -15.6808 | -49.90837 | 2025-09-13 03:49:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e84cd85d-aa87-37bd-866a-bc43620d3b76 | -15.24217 | -44.04413 | 2025-09-13 03:49:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47a6f67e-e170-3e59-aaf9-fbbf3e49f34d | -16.09175 | -49.97028 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb22fb88-88b4-3ab1-8b48-4916be562f87 | -20.61888 | -50.22546 | 2025-09-13 03:49:00 | NPP-375D | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04380b19-c66f-3240-97f0-3555fdf32d7a | -20.64446 | -48.69212 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d1d586-27b7-3134-bb7b-c5f07da7f716 | -21.94475 | -44.85266 | 2025-09-13 03:49:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b90c0158-50cd-34af-9352-08885f238a7d | -22.1783 | -49.61388 | 2025-09-13 03:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6f1cd9cd-6703-3274-9635-0d5307130d56 | -16.25057 | -50.07528 | 2025-09-13 03:49:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d018499b-a134-35e5-83a9-a558dbd7e26a | -16.41124 | -49.23996 | 2025-09-13 03:49:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 599955e2-04e9-3bd8-9d00-757331a01d2a | -22.24882 | -46.14905 | 2025-09-13 03:49:00 | NPP-375D | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 28267db3-152b-3de8-ab1f-baa4b33cff74 | -23.13636 | -49.65458 | 2025-09-13 03:49:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8f1ae777-f144-3975-b81f-e9998c0dfd5b | -22.65819 | -53.12155 | 2025-09-13 03:49:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f926da00-9065-3aab-8a99-d9d77eefa06d | -16.09291 | -49.96499 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38f8d916-99d1-3aa2-8021-4f3da1053fae | -20.60078 | -50.41059 | 2025-09-13 03:49:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d6d61174-12fc-309a-a8ff-079a3d34e27a | -16.05499 | -50.0146 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0281210e-0b23-3df7-a119-a6247cbc8948 | -15.71201 | -50.58017 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dac97d63-b57f-3e9f-bef6-df06e3b00b16 | -15.51026 | -47.29091 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de2ec0ac-27ff-3837-bec4-d5d7582ea7a2 | -21.59993 | -46.92386 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ab173c9-e9db-3d8c-9338-1a88d6eee960 | -15.69086 | -50.58074 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 285da085-6007-3602-83bc-97a8e7ef17ac | -23.46018 | -47.35258 | 2025-09-13 03:49:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96a5b04d-f57c-3ce3-8cca-4d8ca105229e | -15.85756 | -47.23431 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c3b8e2f-a4c0-3f2b-bd9d-c4f9e01a67c3 | -17.71692 | -40.26288 | 2025-09-13 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| ebcc998f-5aed-3e5c-a41f-1afa79eb10b0 | -17.46821 | -43.72764 | 2025-09-13 03:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6633260-24de-33b3-9b85-dd03bf8d0467 | -14.45667 | -47.32156 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa857b6f-eca6-3e74-abba-10c79bdf807a | -21.06836 | -46.14447 | 2025-09-13 03:49:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 14f8e1b3-0a95-330a-9bd4-802028ccc517 | -21.62255 | -46.81647 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| c57b2b49-eeb2-3bf8-851a-89d0f720b291 | -15.74348 | -43.01736 | 2025-09-13 03:49:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db177b23-0a61-3b1c-9860-ee92baed562b | -21.55809 | -45.43314 | 2025-09-13 03:49:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3c18139d-a32e-3127-b57c-c6e81336a581 | -15.23325 | -44.06643 | 2025-09-13 03:49:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2fab761-3c00-3c82-9730-77b3ff60873b | -15.4607 | -47.33598 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 94e82b1d-e8d5-3672-bf23-3190ee2786bb | -17.46899 | -43.72355 | 2025-09-13 03:49:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0d60baa-5148-3970-961c-55aa29583231 | -17.71624 | -40.26693 | 2025-09-13 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 6e043f72-1537-3d76-9218-1485590cfd8f | -21.06372 | -46.14363 | 2025-09-13 03:49:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75ab4134-3022-3576-a175-ff226368f511 | -16.07677 | -50.00753 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30d638c0-1cdd-3bc3-9597-ddd963df9e2f | -16.84452 | -40.86316 | 2025-09-13 03:49:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 73fb4f85-c18a-3bb0-98ab-eca13740217b | -15.6821 | -49.90247 | 2025-09-13 03:49:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b1c73b7-7ca1-3e32-ac99-b7b4b76cbf7b | -14.61103 | -46.3343 | 2025-09-13 03:49:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 281b0e58-7de1-3e96-8975-cbb74f0c3838 | -22.17598 | -49.61231 | 2025-09-13 03:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 134067c4-67d8-3f55-a75e-7d9d20ce2a12 | -15.86252 | -47.23652 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52c7ab8-acd9-337f-b0c8-2484b5a04bea | -16.40789 | -49.04902 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README39.md)
