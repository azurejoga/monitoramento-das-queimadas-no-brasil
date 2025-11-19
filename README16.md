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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39716edc-b5e2-38fa-85c4-aeab618c2aa0 | -16.75725 | -50.6932 | 2025-11-19 04:31:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ab20e51-d966-3193-9ccf-380717ac10eb | -10.87414 | -49.53872 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a49c0374-27fd-398c-86e2-e9b1a045d5a2 | -10.79777 | -47.98334 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3b808ae-f380-37f0-b7ba-ba8aeacca120 | -15.07153 | -43.40681 | 2025-11-19 04:31:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d34f8d3-8d05-3220-bafc-8c31c7f7bba5 | -15.54407 | -55.23363 | 2025-11-19 04:31:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 13203d6e-3be1-3767-b7c8-e7dd3ca1569f | -13.9395 | -47.50579 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1268bbf-9699-3904-b70d-4822695eaca7 | -9.36828 | -48.40993 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d4dff4d-e049-3fec-aa6d-7a02de8c4bf1 | -13.06844 | -49.51056 | 2025-11-19 04:31:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f87e08e5-68fa-3c26-8d4a-a15cb2cbc858 | -13.91791 | -47.42541 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 208a4981-824e-3308-a2f4-658cc5805d7f | -10.74721 | -44.52009 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebfea3c7-184b-3932-8417-68bab112fc07 | -13.43169 | -48.23774 | 2025-11-19 04:31:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10240457-ee86-3d69-89b4-97ddf88c4503 | -10.03292 | -53.75075 | 2025-11-19 04:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73abecd-3cd3-3911-acfb-3e09ebcff027 | -9.37387 | -48.41832 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 341e4935-3f0d-3cb8-9885-3d58f0c2b329 | -15.54206 | -54.34752 | 2025-11-19 04:31:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 385aa042-f9ff-3d13-a5a3-f49276c877b6 | -9.76004 | -55.62221 | 2025-11-19 04:31:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1a7afd2-7eff-3670-8916-487aefceb575 | -11.93959 | -46.58176 | 2025-11-19 04:31:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c5350ce-6b47-31c0-a9e4-5ef30b85223c | -13.88529 | -47.42038 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e44c8970-918c-39a5-a823-15a2a58e0468 | -11.0165 | -49.04072 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61d3eab9-b775-36fd-ba18-582533ecd664 | -13.06597 | -42.13633 | 2025-11-19 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7b08a61a-2c52-3fbd-a456-d06499f1a683 | -10.06863 | -44.86435 | 2025-11-19 04:31:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5daf6c69-9741-3a8b-96d7-9c6685da7332 | -10.10247 | -47.88836 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fc86c18-5061-32b8-9247-8ae4fe3c8df6 | -10.51281 | -44.42501 | 2025-11-19 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d79b893-dff0-3cc7-81bf-5ccf142cdeb7 | -10.64651 | -44.78507 | 2025-11-19 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a2e7eff-9850-38d4-9536-397cb53b5325 | -13.91681 | -47.47635 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6be246d7-76fa-3dd1-b616-ebfc3c7be889 | -12.0035 | -49.2674 | 2025-11-19 04:31:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 382fafe3-8547-3d7e-9f46-579de188b5a3 | -12.53163 | -48.75666 | 2025-11-19 04:31:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7455c527-94f3-3ccb-872b-662edafaa427 | -10.09972 | -49.58998 | 2025-11-19 04:31:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3738fd1-dca2-310c-93f4-9d7b7f34d1aa | -13.8875 | -47.42809 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb4c60a6-c80b-3886-a388-b802b83aaa72 | -10.35346 | -48.90564 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b839daea-7ea2-3d71-afc8-b8f908639415 | -10.0997 | -47.88428 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6e3e8d2-981f-3d80-a5b8-e3ca36f4f924 | -9.39345 | -48.44777 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d9dcf810-64cc-3bba-9429-671c86c10bc8 | -10.05125 | -54.3444 | 2025-11-19 04:31:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52b612b-2025-3868-ba53-91880ea47d2e | -15.87741 | -51.14391 | 2025-11-19 04:31:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfaabca4-8b4f-355b-bbd0-c226affd3954 | -10.35407 | -48.90194 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 13cee67a-4001-3d52-92b5-dcd9c7352949 | -9.38844 | -48.4357 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc95831f-cfdb-3486-ba1e-d18fd062c430 | -9.37446 | -48.41467 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b104bf5-6825-3be5-9663-d4c44ed85e9e | -10.65842 | -49.3742 | 2025-11-19 04:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f48bf0ad-b5b4-3b31-9967-81e618ed04f1 | -13.88197 | -47.41982 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c18950b6-02ee-342f-b99e-d082e93943a2 | -10.84997 | -47.61886 | 2025-11-19 04:31:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b86466c-5ce6-32f6-aabf-93d5fca7312a | -11.51343 | -45.00348 | 2025-11-19 04:31:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fb0036e-45ef-3f1e-b2ac-046450217e80 | -10.8735 | -49.54257 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4527cfc6-ad14-3a00-b0b5-a8b72ceaf419 | -10.35163 | -48.91677 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41225aaf-b5e1-3689-896e-57e5960e2eb0 | -9.37667 | -48.42252 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 789fff06-429b-32de-b599-853645823039 | -10.8798 | -49.54762 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c51a44b2-ef86-36b3-819d-fd67853a51e2 | -10.7805 | -48.83867 | 2025-11-19 04:31:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 935cdd16-513f-3f46-802c-bc344aa27e7b | -9.76514 | -55.6232 | 2025-11-19 04:31:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37e4b20a-3adc-3668-b77f-353fbab452f1 | -10.14048 | -44.19756 | 2025-11-19 04:31:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a20ca92-9e07-366f-a993-3520b9218c85 | -13.92401 | -47.47392 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a31eff9-57db-3674-891a-6005a953fd1b | -13.92123 | -47.42596 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc222894-9e55-31f1-a862-e5805eebc98a | -10.82424 | -48.03151 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 044aec2e-2689-33e4-8946-facbb079c99d | -10.01445 | -48.22091 | 2025-11-19 04:31:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c17b6712-b214-31e1-ae62-4d13c532387a | -11.2042 | -49.41231 | 2025-11-19 04:31:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a851335-96f9-35a2-a31c-d0ab9134d4db | -10.34944 | -48.90878 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a7eee7d-5844-32ba-b20b-0947b924e12b | -13.9002 | -47.49953 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a478e41-57af-3822-9497-7bd5b1cb6bc3 | -10.88044 | -49.54375 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2f367f9-bfbb-390b-8f82-5ae5af80c55f | -10.79266 | -48.61208 | 2025-11-19 04:31:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72ad3172-546e-32fc-a994-ae4ee5cc0743 | -10.0651 | -47.90766 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 834ecd7b-62ec-3baf-a4c0-6d7ad6e32a7a | -14.53307 | -48.01469 | 2025-11-19 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8496c6f-963d-3c79-8df3-e0a5312ecbd7 | -9.40082 | -48.44522 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4224ed57-8ee7-3df8-8702-8e22cfbfccfe | -9.85223 | -48.80911 | 2025-11-19 04:31:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98ac4148-6700-38ad-a44c-4201d4e60609 | -10.35285 | -48.90935 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b17f9292-50e7-3409-af55-3bca28d814a4 | -13.2055 | -48.32057 | 2025-11-19 04:31:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8041d294-8ac2-3de5-a802-779481307b61 | -10.84288 | -56.95974 | 2025-11-19 04:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd53f95f-04f4-39d0-a563-8609f83502c4 | -13.90525 | -47.42366 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a492088b-f38a-3ca3-9796-06bd190854b3 | -9.38167 | -48.43459 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 848ba4f2-f637-3f63-9098-00958f354595 | -10.47229 | -49.1871 | 2025-11-19 04:31:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e904b841-a01a-390e-b16f-247b5a9d31ec | -10.76582 | -48.03941 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9799df49-e6e9-33c4-bba4-7b393a7fb3e5 | -14.80103 | -52.79176 | 2025-11-19 04:31:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f65e9c5d-baf2-3814-aa29-cbf2c74c6e25 | -15.06685 | -43.41147 | 2025-11-19 04:31:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3d49c318-4d5d-3093-aaf0-a4ffc6e62b23 | -18.15988 | -54.55692 | 2025-11-19 04:33:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27f20b06-5349-3637-abe6-67e81f9efefd | -18.5857 | -55.9487 | 2025-11-19 04:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 983088f4-b292-359d-bc88-40e39a0b45f5 | -16.20765 | -58.7443 | 2025-11-19 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 152e26c1-021e-3516-b282-d49963e0ffab | -15.96488 | -58.23277 | 2025-11-19 04:33:00 | NPP-375D | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a67ca517-f348-3893-bdb9-4f2472a2e6ed | -22.47617 | -49.13526 | 2025-11-19 04:33:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d044af51-bbee-3a27-ab5b-b969ff586c0c | -16.20634 | -58.74372 | 2025-11-19 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 26318216-0969-3163-b670-ef90f94f371a | -16.6656 | -52.15285 | 2025-11-19 04:33:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3507b4a3-e225-3011-8d0b-1033d480baf2 | -16.20213 | -58.74296 | 2025-11-19 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dceb14e2-c884-38cc-a54b-42cde08ddf5e | -16.20553 | -58.74752 | 2025-11-19 04:33:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 19e8e330-bfa8-3c5c-bcf7-d0dd423471a3 | -17.53673 | -53.71034 | 2025-11-19 04:33:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 128aae93-7907-302c-9eb6-43e2ee8e4a60 | -22.97884 | -48.66799 | 2025-11-19 04:33:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bdbcd7d-3512-3bd7-a6fe-d68f687a80fb | -18.1558 | -54.55602 | 2025-11-19 04:33:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e533109-915b-3001-8b7e-6c9a639355e8 | -18.5049 | -55.52243 | 2025-11-19 04:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 558dba59-4090-3703-b77d-56ff467dd4a2 | -19.41702 | -45.30061 | 2025-11-19 04:33:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9efe9b1-3df9-31e7-83a1-516562021dc6 | -19.79563 | -56.10161 | 2025-11-19 04:33:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6bb20e86-d868-3218-9bfa-eaa66c17ec50 | -23.52191 | -46.97399 | 2025-11-19 04:33:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad68fe0c-39ba-3c49-8b4a-4505fe54fd0c | -22.18993 | -53.97473 | 2025-11-19 04:33:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d06bf6c2-6244-34ec-8178-830bc5430c4e | -18.92341 | -52.14636 | 2025-11-19 04:33:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa6c5dd7-61ec-3b18-b509-5e51317225f6 | -22.47282 | -49.13467 | 2025-11-19 04:33:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdc1198a-a85f-3b75-be5f-248c6c2d8f9d | -17.53377 | -53.7043 | 2025-11-19 04:33:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02ee5359-d585-3476-890b-0813177538f6 | -22.01126 | -43.33168 | 2025-11-19 04:33:00 | NPP-375D | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| acecdaf3-aa54-39c8-b937-0be34b4140f1 | -22.0114 | -43.33016 | 2025-11-19 04:33:00 | NPP-375D | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c057fe09-bc65-36b8-9fbe-340105c9ab7c | -17.61642 | -54.18101 | 2025-11-19 04:33:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 015007ea-0084-3289-a8a7-d4fa64385687 | -19.24854 | -55.34743 | 2025-11-19 04:33:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9703c415-2da7-37c8-9b57-4e20c7ada452 | -16.65313 | -54.57806 | 2025-11-19 04:33:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb9fd5d4-6bc0-3af0-a02b-3e82210f1124 | -18.50406 | -55.52677 | 2025-11-19 04:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aeb2918a-acab-36df-ad42-b60434d5f14d | -21.57378 | -48.37389 | 2025-11-19 04:33:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bee8fde6-bdb6-3daa-88ac-375ea5b39dfb | -20.75589 | -48.04026 | 2025-11-19 04:33:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b879369-9072-33b9-841f-33de6a3503e5 | -19.28362 | -49.57241 | 2025-11-19 04:33:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94449697-a9fb-3ee9-9866-814e6612fecc | -22.4756 | -49.13904 | 2025-11-19 04:33:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 983f8f35-ddea-3bd2-976f-7229107883e3 | -16.66635 | -52.14859 | 2025-11-19 04:33:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
