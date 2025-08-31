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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14365bcd-a926-3466-be4c-d712e4531179 | -9.68379 | -47.0414 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60fd59d2-b7f3-31e8-b90f-51e7004cd6f1 | -11.35391 | -43.63414 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e7e5a3d3-7321-34ec-bd55-6b1a8044b512 | -10.70744 | -49.01116 | 2025-08-31 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44ba43be-9047-3042-a96e-b994d2dbf2af | -11.36598 | -43.60387 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c0ef686-c999-3ecf-b05f-c76e8ab211b3 | -14.03921 | -44.5569 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5148f35-5c67-37f8-8a36-6212606d4626 | -11.82184 | -46.42578 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4dc074a8-c534-3e43-a856-eff552c32c20 | -14.8052 | -46.72699 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa6440ed-2ffc-33fa-b826-e784840e2379 | -11.90796 | -46.40251 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66150ae6-ed56-38b5-8f7b-3fe83648da47 | -10.60695 | -44.32854 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 557899d0-ae45-32aa-9b77-fa88009fbcfa | -11.26847 | -44.93152 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 388b3df3-bc58-3fff-a042-25a3c0fb50df | -11.88655 | -46.72863 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dbffdf7-a1e3-3ee3-89ad-902eb70a5ebf | -11.81849 | -46.42524 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9817a2c6-5a6d-39b0-9c12-1f26ffd13afd | -11.81739 | -46.43241 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4320df45-bff7-32a1-9eaf-f3428ca74825 | -9.65878 | -48.34853 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a965a0de-ad3d-3f79-a142-f5d5f0c4b129 | -10.0998 | -49.28408 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ddb920f-f07a-3f3e-969c-04d48d2e60bc | -9.58994 | -46.0072 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66d43012-2954-37ef-9d69-738db5cf27c2 | -11.05587 | -44.62178 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 851080b6-9f95-3b0e-bc47-4bcfdb7f8bff | -14.33837 | -51.87947 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4d87c6d4-e645-35ba-b480-04911f0f4924 | -8.96411 | -50.00396 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22250298-0321-3fe5-bb95-61b7c23107f7 | -14.26245 | -48.05985 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b6cd7e3-8744-3bf5-8cbb-e2f582ba4646 | -14.55306 | -51.98088 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a22b18ac-57a0-36a8-a770-b222d1f8dc49 | -14.53806 | -51.9781 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f61ac8bd-bd77-3cee-970f-f92aa7e29d1d | -9.50078 | -49.105 | 2025-08-31 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbbd41e3-c616-3b0b-a8e3-957f07ee9f28 | -11.41859 | -46.91203 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59b8f84e-9d71-3e47-bd3f-8e8360944b78 | -13.31466 | -46.89648 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c781e597-2cc0-3f4e-836a-9b1b24d0b3ee | -9.66335 | -48.34174 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3960b385-1629-3d26-b250-f2a03a8f7985 | -9.58939 | -46.01075 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee7eb458-938d-33e2-9e89-c207c8f94e9b | -12.39824 | -46.48254 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e51486b-ab03-3038-9def-4fff6dfc84c0 | -11.83906 | -51.49537 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 258cbbfe-7b1d-3cf3-8437-ff9647e245c6 | -10.03192 | -48.08952 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 754e6e16-faac-397e-9ddc-36b31d2188a9 | -13.33024 | -46.8623 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ae0b4b1-0633-3443-a560-b1826fec2687 | -13.68964 | -46.87889 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8457744-3fab-3c6d-86f2-6dfd1bb2ca7e | -11.00691 | -46.84262 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b891dbd-bc03-377f-9e02-dc997ba8b3c0 | -11.79877 | -46.47389 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58728bf8-3085-38e3-b951-b5a0b3a011d6 | -14.03372 | -44.56937 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12e5d61a-b614-3e1e-8d3c-25a72874d7a2 | -11.91187 | -46.39945 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a83e961-9fdb-3986-88fc-b82ab802dccc | -14.53644 | -51.98736 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de09df2b-d854-3c3a-90c3-3b1db14bbed9 | -15.77503 | -45.38178 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91882dfe-bd76-3c24-8dff-f9412e1a5979 | -13.02165 | -56.90168 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dbd6c5b-2491-3400-9b3c-7e9d93277f0f | -11.82652 | -46.52932 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9128ddb0-beae-320a-9fda-3e72f54f37f2 | -13.49894 | -46.97001 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f252acdc-b4f5-3a97-b0c6-5b32ca26ed00 | -13.3297 | -46.86583 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2bfad52-d97a-3e9f-a190-5a756607109e | -13.67014 | -46.87167 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88004cb1-b4ad-3e9a-9d5f-c1434431a31d | -10.72925 | -49.58207 | 2025-08-31 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2906309-ca27-3c53-84b0-25c38cc728f1 | -11.00146 | -46.94282 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7268aa4-9695-39b3-b88c-273477c286d0 | -10.03471 | -48.09357 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 16caabea-1b1b-3448-ab88-1830165d07d0 | -11.34647 | -43.63294 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e7b6173-b4bb-3479-a909-9f97db4b743b | -11.8912 | -46.42189 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50d6714c-ba8d-3d5c-95af-b0f67be00b69 | -13.48484 | -46.83829 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e135f92-1c19-383f-a8e5-80f4d7cd57c8 | -10.97135 | -50.86396 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66e0da76-1556-3b4a-bfd2-7304fdc06e2b | -10.0345 | -46.01856 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 171dcc06-bb27-3bd8-9ed5-b47ce340fd93 | -13.97076 | -46.32091 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a52674-80d5-3195-a51f-30546c020821 | -10.08306 | -49.27726 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 456528b1-ae8a-3b3c-95d8-9d80abc7ab13 | -11.21027 | -45.03384 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6bb7f5f-903c-3f20-b52e-d36e025375f2 | -11.78984 | -46.46506 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d13cbe8-4d8c-3224-9976-8c8f673dbc44 | -14.99351 | -46.69972 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90ab5093-0845-3c4f-ac6d-ac97b71c34cd | -12.63172 | -48.20372 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fb4b6d2-75b5-3aee-8ff2-9fbf8702deb2 | -11.82355 | -46.43705 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71f07f70-98f9-3ca8-b329-6fe21f958baf | -13.02552 | -56.8884 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11b7534e-53ed-3ce5-802f-5b725778cfb3 | -11.94386 | -46.69027 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98794638-36c5-300a-b798-fdd1b3300d0c | -13.47497 | -46.96971 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b13eee73-e29d-33d4-b626-91461c787ccf | -11.31944 | -43.6879 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4fcc921-9f4d-37a4-a913-485bc9247fee | -13.31359 | -46.94786 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37135922-5f93-34bb-8606-151f4c6e3aa6 | -11.07586 | -44.63311 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2359b449-c019-31a4-90a7-ab0ac29836dd | -15.94299 | -41.39598 | 2025-08-31 04:29:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25f50862-eb36-3d31-b0c6-b005b5b62514 | -10.95431 | -50.85181 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 022aef5d-0345-32cd-88ca-a4ac241e0a60 | -11.5579 | -47.61761 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 422878f8-ba80-3858-9b95-9db68e9dfb3d | -10.67881 | -50.53456 | 2025-08-31 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58c90858-9392-36b0-b40c-ae0b4b5bff93 | -11.01312 | -46.95552 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eef5fb9e-b981-3ae0-a77e-d46390f83a3b | -11.81665 | -46.42519 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ba45499-8c62-3113-bc44-595ab2a2a65a | -13.52182 | -46.97733 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb682ccd-c314-3777-91fe-66356350a8e5 | -15.0785 | -48.62416 | 2025-08-31 04:29:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11580fa1-7f16-3791-af4c-a94fc26e58c7 | -12.09056 | -44.72354 | 2025-08-31 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 307ed430-eef9-332d-9207-5e3b0b5509d2 | -13.26034 | -51.9815 | 2025-08-31 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 625cf067-b424-31bf-819e-648cf7dacebc | -13.26417 | -51.98214 | 2025-08-31 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8119627-483e-3b9b-9291-4d24913efc14 | -13.31298 | -46.88514 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53c53818-c6d2-3eba-a6fe-cbf3387a3c8b | -9.43348 | -48.33809 | 2025-08-31 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1079c08-2d02-3b73-8a6a-18dde14faab3 | -15.67353 | -43.22632 | 2025-08-31 04:29:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 51376a80-960b-34d2-9dde-07983118c0c8 | -12.80538 | -48.09326 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f42922-3621-3f89-8e20-80dbe48ffa3f | -13.68401 | -46.89298 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae39cf26-f19e-38e9-b863-24810a10952d | -11.81519 | -46.44675 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4625a3dc-fbcd-3b81-8200-213700ef3aa7 | -8.96995 | -50.03358 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 215d81a6-9493-3ba9-a781-e785dc283476 | -11.35216 | -43.62011 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b8de38d-729c-3904-ab68-fbb6d2432a36 | -13.48605 | -46.94241 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5f6bb2e-b8dd-374f-a6b6-bc283cfa4887 | -12.91512 | -56.9761 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbbeac7c-b844-3090-b291-cef9d53c4c48 | -14.49734 | -52.98642 | 2025-08-31 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06244204-e838-366c-a119-44ac660afa83 | -11.31202 | -43.68681 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32d019d9-52a1-33e9-8db0-38fe1734f282 | -11.82762 | -46.52218 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd639bac-46f7-3383-a3a8-d262edfae888 | -14.80912 | -46.74706 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e40b0c9-327d-3882-a2e6-848c293c1dad | -9.4913 | -46.70219 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab2bd09a-f769-3eb0-9909-6151a3b70c60 | -11.87855 | -46.72417 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 525dd654-7de0-356b-8a3e-9fb85715adaf | -13.02489 | -56.88539 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c28ea150-748c-32e8-89b6-780f24b02b95 | -11.86052 | -46.48698 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b4d33f2-d032-3be7-86e5-a7286f0cb8b2 | -11.08005 | -44.60513 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e20f9895-ec21-301d-96ea-8f1eb15ab920 | -15.96438 | -43.8989 | 2025-08-31 04:29:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f18c30bb-66d9-3419-928b-0065e0ec5afa | -11.33969 | -43.62729 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55bafc76-5fe0-3126-97eb-d3614037adee | -13.62928 | -49.84052 | 2025-08-31 04:29:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28be0775-f2fc-36bc-9751-e674e4c25f64 | -10.95506 | -50.84737 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1300b4e3-8f3b-334d-bd5f-b92fa3597de0 | -10.95061 | -50.85117 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b7e7bde6-1908-37e0-b138-198f2148b52e | -13.37484 | -46.96109 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README43.md)
