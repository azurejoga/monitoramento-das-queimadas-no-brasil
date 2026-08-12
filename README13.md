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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c9ca2db-f0b7-3dd3-a034-329a6d0d09e2 | -11.95034 | -46.35417 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 119c7530-6e47-30e5-ab93-915115bc3f28 | -11.82872 | -51.85239 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb5d44fe-9454-3ae1-b4ef-12263212d43e | -14.39999 | -52.07313 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 89090ca3-e7ed-33ef-acc2-9c6cff73060d | -11.90513 | -40.65478 | 2026-08-12 04:17:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b106d501-892c-3b41-9a14-1a1cdfa7ea8f | -14.54993 | -50.39788 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a850909f-50db-33a6-aa6f-c09eceff2f54 | -11.98021 | -46.38619 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8ee4f8b6-535d-3fb1-80d1-482c5a1b4ce6 | -11.4689 | -46.61118 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2ae2dd7-dd5a-3574-8a5d-688da8914e84 | -14.28067 | -45.27804 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eeeff1f-f9f9-34f7-a5b2-ca5f9390400b | -11.95501 | -46.34708 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 37e9da7b-54e7-3ca0-a504-2b10debce747 | -9.33098 | -47.53793 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9f0647-c6df-30e9-bb87-b90e11c1c435 | -11.98426 | -46.38291 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ee12c85-754e-3b9b-ba48-d38ec4548aaa | -11.8233 | -51.84391 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c3288eb-1764-3f5e-a729-a9d3e0d2bc54 | -21.53742 | -48.64312 | 2026-08-12 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbd2d058-b6b3-30fa-8c68-4d5006a00667 | -13.29817 | -49.70184 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3865390a-2ba2-39e1-8c5b-1b30ec17787c | -14.51208 | -49.29074 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c7b255b-a686-3b99-9348-64638f13f740 | -9.92478 | -49.26766 | 2026-08-12 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba9a87b0-6a6a-387e-98d1-5acdcf16258d | -9.15782 | -48.83632 | 2026-08-12 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b04def2-4a59-3bf4-8d05-ba151eca1449 | -13.37819 | -41.34471 | 2026-08-12 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5a68048-9485-38da-be81-f97b22c63656 | -11.60847 | -54.66071 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 21268b6d-1af1-3285-ac67-e34a074a7ab4 | -9.03406 | -47.49733 | 2026-08-12 04:17:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec1daff0-4a31-384d-987d-1b66af0187c5 | -13.30502 | -49.69983 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1e5a35ca-4d16-3b63-ae10-883768b51bc6 | -11.81663 | -51.82728 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc85ccbe-c00d-3604-8657-785261b69821 | -13.88803 | -53.82716 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4851bdfc-3706-312d-af2f-6dde616fc9d4 | -11.96619 | -47.31366 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab62860d-050a-3689-a551-4247cd5763f5 | -15.17055 | -49.26611 | 2026-08-12 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a942232-3441-3aff-8667-4bf58b6c9bf1 | -9.36953 | -47.44438 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8c65622-d0d3-304b-aa97-ff2b73b4a1e7 | -15.28272 | -48.86168 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a7945e-18da-3188-a90b-55779abb808a | -14.99795 | -46.60287 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468add0a-1b65-3807-90a4-279e5c0e5161 | -11.94792 | -46.32617 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 58c98cff-5f4d-3adc-b5be-4ed17cdf79bd | -11.47277 | -44.5577 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1fca6d74-8144-3f35-ae07-5186c4a41f25 | -16.1025 | -49.89389 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dba383b1-d331-37c3-b36a-42af9a2ec003 | -11.81552 | -51.89682 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f43f0a37-f1bc-376d-9782-f1ff32297c1b | -14.03673 | -53.59568 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c2c6083-854b-3734-8953-2748309ca4d7 | -14.33822 | -54.0489 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f0403e63-f2b6-31e6-9208-9fd8c25ebf43 | -21.30827 | -46.73272 | 2026-08-12 04:17:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1ef169cd-4999-349c-9747-31ad119c533f | -11.47235 | -46.61179 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c39c1bba-7a24-3e65-9452-9707323c4692 | -10.3621 | -46.38042 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3a433a8-5f0e-3c66-be81-771d547d16e6 | -14.36131 | -53.22846 | 2026-08-12 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e3da42f-14a2-3bc2-83ce-15ab538981da | -13.30124 | -49.70778 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| ae071aa8-5905-31a0-8b2b-d44db8746a7d | -9.36878 | -47.44881 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd170330-c5a2-30bd-bbcf-7cc22c90be5e | -11.93745 | -47.35514 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b5776e8-9e4a-3f7a-945c-495db568cd0b | -13.84227 | -53.77838 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3999e52b-2dab-3217-842e-8c3e0fea7530 | -21.41709 | -43.87886 | 2026-08-12 04:17:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8fa9bf23-d0d0-3cec-8e28-96b79170f391 | -10.42338 | -46.32349 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5758547-0639-3b65-a54c-2006541fa73b | -11.84039 | -51.88353 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9c3d6d7-afc3-34e0-836e-75eb06775be1 | -11.95347 | -46.37794 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a87a61f-0b26-3032-8e18-03a228e65719 | -11.46506 | -44.56366 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81db74d1-07b2-3b96-ae22-352db53f44ac | -11.95909 | -47.31246 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 655f9979-92fd-3c9c-8265-88cb046cf1cd | -14.97718 | -46.60291 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1a1f361-70b2-3798-b3ab-a299f8dfbf37 | -11.98364 | -46.38673 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 034f69f4-3fb5-3eae-92cf-19da521aba34 | -10.09761 | -46.2313 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 824cf0d8-29dd-331f-b581-8e34c1f2fc1b | -12.55636 | -48.35009 | 2026-08-12 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18328bd1-a40e-3dea-9023-31b0084ab37a | -14.55332 | -50.40241 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fba57089-6a52-3d04-8831-845b8549e628 | -11.49935 | -54.60527 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 113b296c-3dab-37f2-83a0-1259afd5da21 | -13.28624 | -49.6294 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8add101d-11af-388d-8073-d12c48e9ecdc | -11.55708 | -50.23058 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cb2de7f-15e4-374c-9465-89185804d30a | -11.97276 | -46.38886 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5b6c955-581d-33eb-9c5b-6bc4b0c9cc5d | -9.34586 | -47.49487 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1dd704ab-da8a-314d-b0e4-1e5fc267374e | -14.51667 | -49.28696 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db6713f2-105f-3c17-b026-fe3cedea3e6e | -20.96554 | -47.41396 | 2026-08-12 04:17:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 626f963d-e36b-3351-9371-d8cca982c5e0 | -11.46415 | -46.61842 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daca75f4-b7d2-3c27-b514-c250b954e670 | -11.47774 | -44.56929 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| cc495ef8-19dc-34f0-a739-7ac821510db7 | -21.4959 | -48.63923 | 2026-08-12 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f0929b9-b15f-351e-b4ff-ee6cfb7c442a | -12.27609 | -41.60252 | 2026-08-12 04:17:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7c6d7035-b35e-300c-b5af-6241d47476ca | -13.8975 | -53.8333 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b1614f-b7c5-39b4-823a-a6affb51bfc6 | -10.63533 | -47.48949 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 262588b6-9f3d-3e07-be2a-1fd76e4cf856 | -14.58716 | -46.75581 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5e0b611-e174-3e45-aa56-e141d126bc23 | -11.60997 | -54.65288 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db52382b-2f6d-3246-bf1e-d15603bde1ed | -15.30065 | -43.81216 | 2026-08-12 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93fa389f-1bb0-3d3b-bd08-3a4ec3ce9b7c | -21.76298 | -46.69446 | 2026-08-12 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c4573796-6543-38bc-9212-55926e0ed5e9 | -14.98569 | -46.59311 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1ffce28-d084-3e02-85a1-925fef86a560 | -15.01199 | -46.60166 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9774517b-ee3f-3bbd-829b-e1c60679efea | -11.97152 | -46.39644 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30af9d16-a904-3b1b-9719-33b2939679c3 | -13.90897 | -53.8292 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03fa40f1-78ff-3c8b-a4a1-62fea58576c5 | -22.26944 | -48.66095 | 2026-08-12 04:17:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8507d0fd-eefe-31b8-a7a5-4800653f3f1a | -13.564 | -47.63889 | 2026-08-12 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c236be57-1075-3266-a278-d03d75b8c4c4 | -12.14261 | -48.2661 | 2026-08-12 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80389dbd-5ae9-38c6-9734-7a0c5a159637 | -13.83189 | -53.83247 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 898090c9-b7d5-3a0d-9fd4-456cd93805b3 | -9.13308 | -46.39692 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 410cf200-1315-3ec6-b465-36abef6a0a3a | -14.52084 | -49.30794 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dfe4c9f-5505-3576-9635-9563f062d386 | -12.47718 | -44.50458 | 2026-08-12 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9c89ef4-8540-3cb9-87c9-bb8fa255ddca | -12.09903 | -47.18932 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88abef51-16cf-3871-b9d4-df2bda850583 | -11.81195 | -51.82647 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cb1a195-b401-398b-bc25-89cd520d79b6 | -13.87411 | -53.76246 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b3e45a4-8e57-3b5d-a01a-3b959754984f | -11.80819 | -51.82055 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dd0403f-ba14-3626-99c0-f58c6c59a8fb | -10.35856 | -50.40645 | 2026-08-12 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63c3af86-0cda-3adc-b604-eef6e9ce0930 | -10.89717 | -50.17336 | 2026-08-12 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1ff40b0-d552-3080-825e-da9d35e60fe5 | -14.5129 | -49.28609 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec718e86-81f9-3741-b863-3984c70b8723 | -11.82615 | -51.85492 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b4c0037-6a78-390b-a86b-d53a6b0eb048 | -9.15744 | -48.9606 | 2026-08-12 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fd3bd6b-d38a-3351-8efb-cf6fe341f9ca | -14.5486 | -50.40532 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b9c6f66-fcfe-3642-bec3-7d13e86e2f69 | -13.89875 | -53.79958 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 436684c2-dd2b-3608-9b72-994e2d4d14ae | -22.45862 | -47.00765 | 2026-08-12 04:17:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 611c1582-77a1-310e-bbf4-fe17318a710c | -14.58932 | -46.76388 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86aa9828-157d-32e4-a868-0982cbc7923e | -16.34311 | -49.46455 | 2026-08-12 04:17:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11aae223-2356-31de-bf02-2b2d04fa7dd9 | -9.32929 | -47.53491 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5e6ed38-4efe-3573-949a-a1b43a3501a1 | -16.10606 | -49.88606 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 28e6e93e-13f5-33fa-9b98-4b89a6f0b4c7 | -16.67735 | -45.03643 | 2026-08-12 04:17:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e613de39-85c6-3c5f-842c-0e0af7b016d7 | -13.01995 | -40.34629 | 2026-08-12 04:17:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22f19ed1-aabc-3341-90df-e27c782e7f79 | -13.85559 | -53.82018 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
