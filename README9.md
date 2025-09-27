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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b5f97e2-c341-39e5-9bde-c64463f120cc | -18.41 | -51.7494 | 2025-09-27 01:40:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fa87d491-bf4c-3762-a2c0-2cbced8358cb | -5.4937 | -43.0761 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 268.7 |
| 5971d1ea-9136-3e7a-ab49-c3521db9ab30 | -15.2756 | -46.4468 | 2025-09-27 01:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 02064b93-8c33-3df8-be07-50fd58270d4f | -15.0462 | -47.1274 | 2025-09-27 01:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 247.7 |
| a50d5395-d08b-385d-8a6e-769b2398f725 | -22.6001 | -48.5934 | 2025-09-27 01:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| 038cb48c-d8d8-3fd8-a9e3-1e6656502449 | -5.4752 | -43.054 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e65df250-b276-3470-b286-1d7e6dcc4aca | -5.4935 | -43.0995 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1a7172bf-0bd1-3845-9b1f-afa90c272903 | -15.0457 | -47.1502 | 2025-09-27 01:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 393094d7-bbd3-3789-817f-c311a73148ce | -5.5243 | -43.8647 | 2025-09-27 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 7497e614-dc8d-3144-915e-e39b4546559a | -22.5582 | -48.6038 | 2025-09-27 01:40:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| e029d14e-b9f9-3b4f-95b2-67764efe3e31 | -5.4562 | -43.0788 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8825559b-b057-3de0-ae6d-c0a4de67d172 | -12.2829 | -44.0568 | 2025-09-27 01:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| fb16341d-95ef-3b98-a0e3-5a3f2987bad0 | -5.5125 | -43.0747 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d6cad978-8486-38a1-b77c-71eff2308b56 | -5.5241 | -43.8878 | 2025-09-27 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f928645e-5d06-3e58-9bd5-548126278658 | -7.1571 | -45.5158 | 2025-09-27 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 014378c6-4c07-3afb-8ca5-0fce0c62c344 | -5.4748 | -43.1009 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f6ff4932-0c51-3f36-af23-0631ac325cb0 | -5.494 | -43.0526 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| ffe60777-7aed-3894-82ce-4fe238a0af2b | -5.0862 | -44.857 | 2025-09-27 01:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 35878864-4a21-3c6e-825d-929034462b3d | -14.8448 | -45.6246 | 2025-09-27 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| cf1af3f9-ac4c-32b3-bb5d-90b30ad1a85e | -15.88777 | -59.32908 | 2025-09-27 01:49:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 629797bb-d891-3320-a253-798bc77200bc | -12.17234 | -64.10339 | 2025-09-27 01:49:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1a976072-43d6-3306-85d6-aafded3119da | -18.32062 | -57.11155 | 2025-09-27 01:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| cc66d7db-68a7-3be1-bb1c-c1626473e7e3 | -12.07929 | -63.96323 | 2025-09-27 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 117e2ba3-76f5-331c-9ca8-c9867b036a17 | -11.72598 | -62.58521 | 2025-09-27 01:49:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0533dc31-867d-32f6-9ae4-2fd11f9df989 | -11.3646 | -45.0108 | 2025-09-27 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a41eb3ec-b73f-3551-9d6a-8a630fb3b8f5 | -12.2829 | -44.0568 | 2025-09-27 01:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d55eea02-5bda-3965-84a2-dc8453765261 | -5.0862 | -44.857 | 2025-09-27 01:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 664a16bc-6055-304a-a328-6a593a22d509 | -5.5241 | -43.8878 | 2025-09-27 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| b6808325-4216-3591-972e-0485472b6561 | -22.7271 | -51.3948 | 2025-09-27 01:50:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| 5a94413e-ae0a-341c-bb2c-f8ff32c66b5f | -5.5243 | -43.8647 | 2025-09-27 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 8744ac55-efcb-34ff-b8ff-1d99b2a67fa4 | -14.8448 | -45.6246 | 2025-09-27 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f54a4d04-af2e-3991-87ec-df1b02a907a1 | -7.1571 | -45.5158 | 2025-09-27 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 9f08f388-3315-317d-8020-2832a6c5374f | -14.8253 | -45.6282 | 2025-09-27 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e701a442-1fa4-38b9-9d64-157c26989139 | -9.0583 | -45.5085 | 2025-09-27 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 40aab2ff-4c17-317e-a9be-ab85208b606f | -5.7961 | -42.8182 | 2025-09-27 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 56e60169-b67e-3706-9f60-be2ea41319c3 | -9.0587 | -45.4858 | 2025-09-27 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 541247aa-e5e0-3af1-b5f2-353a350ed33f | -5.8149 | -42.8167 | 2025-09-27 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 5c8c8083-d4f9-3c76-951e-45676cfa8aa8 | -10.6082 | -49.6469 | 2025-09-27 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 11f9cdac-9511-30d5-8edf-781f7e9f4d4d | -15.2756 | -46.4468 | 2025-09-27 01:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 01d22a4a-08b6-3ce2-ba7c-ea85523f831e | -10.15112 | -66.96737 | 2025-09-27 01:52:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a5482370-ef1c-37df-94a3-e9d72418c509 | -9.92245 | -59.92566 | 2025-09-27 01:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| d8c41093-af43-3918-88ca-a80cee75d82e | -9.0583 | -45.5085 | 2025-09-27 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 373.1 |
| 124922d0-1def-38de-93fa-f725e9135d38 | -5.494 | -43.0526 | 2025-09-27 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| cb062bf4-24b9-34d6-8bc4-a0e186fbbd29 | -22.5792 | -48.5986 | 2025-09-27 02:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.8 |
| 85d91d0f-4596-3b82-8ea5-1e095941a86d | -10.6082 | -49.6469 | 2025-09-27 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6da7b885-1a6a-3360-9218-ae2c59bc505f | -22.6001 | -48.5934 | 2025-09-27 02:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| b585a1b5-8bd5-3a66-85cb-7c56044f55a3 | -22.5582 | -48.6038 | 2025-09-27 02:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.0 |
| b30aa366-dc3e-3b94-b442-29ad8d493b41 | -5.475 | -43.0774 | 2025-09-27 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| adfd97b4-faf1-3c61-974c-d46998672441 | -22.5575 | -48.6273 | 2025-09-27 02:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 78e0b60d-a652-36b0-bede-ee79faf0c39d | -5.7961 | -42.8182 | 2025-09-27 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| a8ba4294-63ef-3b6e-b386-a0098a79a26f | -5.5241 | -43.8878 | 2025-09-27 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 11941cec-3204-3b0e-bca4-1e84b9c60060 | -5.5056 | -43.866 | 2025-09-27 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| ad846d9b-5bc3-3f85-8d32-a004279cb6ed | -22.5799 | -48.575 | 2025-09-27 02:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 9123aa7e-cf90-396e-b1d7-52b851a95d04 | -5.8149 | -42.8167 | 2025-09-27 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 3bc4ff85-99b0-3794-aed6-f8a706b4b534 | -9.0397 | -45.4879 | 2025-09-27 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 48f0776d-54ef-3dea-806a-608194c22b7e | -9.0587 | -45.4858 | 2025-09-27 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| d3742129-3dc5-3943-8ca1-ed32936126c5 | -22.6009 | -48.5698 | 2025-09-27 02:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 33fac849-dcc5-3d1f-81d6-7cd133ded159 | -9.6159 | -47.5741 | 2025-09-27 02:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 70871ca7-8f15-3328-8f99-791c1ab2c01b | -12.2829 | -44.0568 | 2025-09-27 02:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| cd2a9eef-bcdc-3feb-9674-f5e32b04ef95 | -22.7271 | -51.3948 | 2025-09-27 02:00:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.3 |
| 36670066-8a8b-364c-864a-11b5a4124d8a | -5.0676 | -44.8581 | 2025-09-27 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 14ca79c9-710f-33d2-9896-d8c7249bc015 | -5.7959 | -42.8417 | 2025-09-27 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 6dd54cc2-6375-3946-b9ae-0fe0c911504e | -5.5243 | -43.8647 | 2025-09-27 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 41c26bd1-56ae-3ff6-a924-71233b43fef3 | -12.2636 | -44.0599 | 2025-09-27 02:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| e610fe6e-7d82-3a46-99aa-5e1968c08f42 | -9.0394 | -45.5106 | 2025-09-27 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 1c718f05-c042-3dbe-9cf3-637c9d709f40 | -9.0773 | -45.5064 | 2025-09-27 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5f6c389c-2123-32ae-b6fc-e557307a1d64 | -11.3646 | -45.0108 | 2025-09-27 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 66f48e75-1073-373e-b670-927f2214cea2 | -14.8448 | -45.6246 | 2025-09-27 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f36a6c46-98d9-3f58-a38d-2a56943f1a93 | -5.475 | -43.0774 | 2025-09-27 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 823d9719-fe92-3bcc-9248-8cb27cbde0c9 | -9.0394 | -45.5106 | 2025-09-27 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 2bcb2b22-6a5f-369f-9442-98b3f424c793 | -22.5582 | -48.6038 | 2025-09-27 02:10:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| affe0c33-74c0-30cb-8afd-fe55e8c95725 | -5.5241 | -43.8878 | 2025-09-27 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 0a612b91-d290-3930-921a-5c2fcf9ed699 | -5.0676 | -44.8581 | 2025-09-27 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e7a3e1d4-5c30-3d1a-aad6-0d7e19d3046b | -5.7961 | -42.8182 | 2025-09-27 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 27784e37-eca0-3a9f-b8f8-60ead58bd2a8 | -5.4752 | -43.054 | 2025-09-27 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| dc4a6f1c-2d3a-3a65-a026-0c09c3f8f8dc | -9.0587 | -45.4858 | 2025-09-27 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 36ea3db7-6fc2-31ab-b5b6-d49b87c23f01 | -22.5792 | -48.5986 | 2025-09-27 02:10:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 27f8d2ef-f994-3932-9a68-22b336750561 | -9.0583 | -45.5085 | 2025-09-27 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 198.4 |
| ea696489-4b84-350a-b1e3-7bd10e44ba4a | -5.5054 | -43.8891 | 2025-09-27 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| efdd58c3-e96a-39be-8b1d-48f2d48bf3f7 | -5.4562 | -43.0788 | 2025-09-27 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c885b388-8ae8-329a-b08b-7aabe9481a3c | -16.3548 | -49.9477 | 2025-09-27 02:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 3f68f33e-a88e-317c-8155-1b209428649e | -22.6009 | -48.5698 | 2025-09-27 02:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| fbcafa7a-b1a7-30eb-9a2d-31845c35dd64 | -5.7959 | -42.8417 | 2025-09-27 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| ffd5130c-0889-3309-99f2-b2d79f54ec6d | -16.3351 | -49.951 | 2025-09-27 02:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 2d9ff234-9e06-3e84-9e89-822b627b4675 | -22.7277 | -51.372 | 2025-09-27 02:10:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 19c6bbf4-936b-33f9-ba9b-2001e2a0bdf0 | -5.8149 | -42.8167 | 2025-09-27 02:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 968d55e5-3bd7-368b-b01a-91df709b011e | -5.5056 | -43.866 | 2025-09-27 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| f9eac91e-c74e-3b87-86b5-fdf4deb36702 | -5.5243 | -43.8647 | 2025-09-27 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3d509297-c332-3812-9c62-b6a5eedfd252 | -22.7271 | -51.3948 | 2025-09-27 02:10:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 175.4 |
| c75e246d-c3b3-3263-98ea-a93cc0616104 | -5.0862 | -44.857 | 2025-09-27 02:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| dc551f62-8b63-3497-8d6e-2c304e182b16 | -5.4752 | -43.054 | 2025-09-27 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 1be8034b-a15f-3f64-b313-b292e514caae | -5.4937 | -43.0761 | 2025-09-27 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 8ad5801b-638a-3a20-9c8c-b2340385b9ec | -7.1571 | -45.5158 | 2025-09-27 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 64a7682f-e407-3da7-8bca-cfeb6798a099 | -5.494 | -43.0526 | 2025-09-27 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9c6756f0-448c-33ef-adce-34bbfa1918bc | -10.0062 | -46.7081 | 2025-09-27 02:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 193.3 |
| afecffc4-99b0-3e17-88f6-58e1e191a30b | -5.475 | -43.0774 | 2025-09-27 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 1e10127c-9999-3c1c-8535-0757979fad82 | -5.4935 | -43.0995 | 2025-09-27 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a213fc82-56e9-3c30-a1e9-ed75d46514c9 | -22.5792 | -48.5986 | 2025-09-27 02:20:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| 143d6481-8fb5-3eb0-a46e-86c8f45b73be | -5.5243 | -43.8647 | 2025-09-27 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d77958fa-67c6-32c1-9365-35a2c35b1baa | -9.0583 | -45.5085 | 2025-09-27 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |


[Clique aqui para ver as próximas entradas](README10.md)
