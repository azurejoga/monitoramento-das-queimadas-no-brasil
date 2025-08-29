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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce0219a4-75aa-3dc5-abb3-22a719e577c6 | -12.99881 | -56.92407 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e157871d-12f3-3933-9cf8-aebf3b173f2e | -15.7856 | -48.19534 | 2025-08-29 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41f7b615-73da-310a-b9bd-63d3888b229a | -9.12223 | -65.7634 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92ae2159-7c5c-388c-be98-685c259378a5 | -8.18609 | -61.37517 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 212806bd-2e89-355b-b46c-69abd4f17a08 | -12.81167 | -48.17419 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dde378e-50a9-3c10-86d4-1f77fe1c408d | -9.17491 | -59.45271 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7031e097-016f-3e94-a717-b15498758e0a | -12.85281 | -48.13995 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 206db779-2b28-3f98-a813-7624c787e2d3 | -8.17725 | -61.37743 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d02326ac-d56a-3a57-bd88-84d21ff7e0a8 | -14.36012 | -52.10712 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cfd2222-7f90-3f45-8707-ed9fd72517b9 | -9.10324 | -65.74525 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c20bc42-640b-3161-b85d-2357092666bb | -11.16292 | -47.15056 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc2846c8-3410-38d9-a6b2-a52e4c9859ca | -13.51447 | -46.85608 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f4f24ec-c380-32a7-8a33-09da0b12e6d4 | -13.54194 | -46.87202 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0f81b48a-cbf2-356c-8dc5-e44ecdd7a21d | -8.17853 | -61.37008 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c236ab07-032d-30c1-9637-624f973a3be2 | -12.93279 | -56.97511 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2a4eaa7-6d14-3c40-917e-d11a9a20a5b8 | -13.0159 | -56.91556 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c325ff3e-3e34-3870-b888-b816baa9fa3c | -9.132 | -65.8011 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0ed70be-3b59-3f00-b68b-d5374247982f | -8.29354 | -61.40479 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7605e999-975b-3a42-98f3-b68fd371fc44 | -10.95155 | -46.88446 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e528e8f1-8e20-35b9-b381-9b0029c161b8 | -9.31643 | -57.69925 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1380ff7-cc1e-3a85-958a-4bddc66dc8a6 | -15.66992 | -52.75056 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 768e5a0e-2501-33b4-be0f-293687566afe | -8.27585 | -61.4093 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ff421c-280c-389c-ace6-206399840140 | -9.1941 | -61.02414 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23534b2b-c019-35fa-859e-bd0c7ab54193 | -11.61351 | -46.20682 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc354a8c-13f4-305f-a187-5436c67a5761 | -13.55695 | -46.89185 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 061d27d5-ef71-32a7-a9e4-9644215880d3 | -10.36748 | -57.8329 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8fac77f9-e1c8-30bd-b4d7-e36dd7eb6c01 | -10.98674 | -46.85644 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2bbe085b-417d-3e7c-b748-a668c0d15fc2 | -11.5802 | -46.37384 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 441463a7-38d8-3827-a2b9-984d295955b9 | -12.82625 | -48.10063 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2c57375-28cd-30ce-a74f-923e7da0d273 | -8.95909 | -65.97198 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f89372-6fbb-3459-8e0d-758aa2ebd3bd | -15.5368 | -54.26884 | 2025-08-29 05:08:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c57fd40-2c58-30f9-958c-51d76cb85072 | -12.22219 | -64.22805 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5efe7870-24e4-3061-8666-4b5ca21c4758 | -13.55947 | -46.92092 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 107181af-a7f3-3a37-85de-206f5fb23b7c | -9.5444 | -62.39342 | 2025-08-29 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83e6ad55-46d7-3bc4-ba63-61a5cdd58cf3 | -13.52143 | -46.94672 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcb0fadf-29a7-3f43-b2d7-b61b314c2588 | -9.54094 | -65.69849 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9b3eb99-4a4a-3c76-a517-c3c28db8412d | -10.85697 | -60.81042 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56c53107-0269-3815-8a4e-96774d156a7b | -13.01379 | -56.9156 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 750c7d7e-6248-37b5-963c-d3860bbadf63 | -9.59818 | -55.37322 | 2025-08-29 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d1b46ec-7bba-374a-99c2-aba47c85b797 | -13.00658 | -56.91806 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a5b255d-ad4d-3ec8-8bda-b495680246ca | -9.11228 | -65.78647 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19c04c98-2eeb-383b-8a0a-00cd574bb6fb | -13.17224 | -50.58623 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41d3047d-db82-3c4b-a05b-859b9347364e | -9.16021 | -59.56281 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51e8db78-57ff-3175-9d48-216e095de903 | -11.11994 | -45.11772 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dfae8f8-1074-3af0-bf35-57d26270bc5e | -11.0899 | -44.75048 | 2025-08-29 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4dd20c2-291a-333f-bdb4-36334f809038 | -12.70898 | -48.19152 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5edb339c-3545-3058-98fd-41b9e5c90ec6 | -9.20006 | -59.54791 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c27624a1-1580-3901-aa68-2effb4c6f186 | -9.1684 | -65.78642 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d7de598-00e5-308f-aa4c-323b8eba57bf | -12.69675 | -48.16132 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d43259a8-3819-3576-8492-a11bc125e424 | -12.68758 | -48.19204 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 24af1d19-4e55-3524-b4dc-a739f91d9cb2 | -12.91288 | -48.13148 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e2d3695-12c4-395c-90d4-9392b7bc7be9 | -10.97854 | -46.9237 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 8a3924b1-88de-3a12-a3b0-ceca9aeff18a | -12.69721 | -48.15765 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b0431fa-6c61-32b6-a187-0bc9470d916d | -9.5362 | -65.69413 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a964cc08-33ca-328f-accc-345c9f992eb1 | -10.83975 | -47.50107 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d90f1db-a426-3dfa-a0a5-e72a92b2e1bd | -12.87979 | -48.1387 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea4d0bc2-8286-3797-861e-984f087829e5 | -13.41399 | -46.96513 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e615021-2568-33f1-9016-068d33431fb4 | -9.15151 | -59.57012 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9eec77cb-e672-38b6-9101-5cf922c01725 | -12.70822 | -48.19753 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5c8dc93-edc5-324e-b4b4-748193fa9a34 | -9.45811 | -60.57407 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 44847a0c-68b5-3154-8345-48db27814b3e | -13.4168 | -46.97963 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 208ab920-4d46-33ec-9513-d7f66c316e66 | -12.61898 | -57.01448 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ff800b6-d300-3bc7-bdc0-10ec201938dd | -9.45669 | -60.55905 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 58d7e296-51c5-3572-aa8d-3632f8bc8018 | -11.46151 | -47.30843 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c960b79c-dc45-31bb-9fed-357cbff63c6f | -9.10734 | -65.77952 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0cd85d8c-e7ff-3ebe-9ebb-b6959d83fcc9 | -14.33979 | -53.32693 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a73dd196-a018-38c2-8dcb-401485864d90 | -9.11554 | -65.76917 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7f935ff2-4110-3c7f-9962-c93df3395bbe | -9.30448 | -56.81805 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52ccf3f7-761a-31b6-b4c7-32f8bd82d728 | -13.62564 | -48.25056 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58d429ea-842d-3672-9167-9c31276983c5 | -11.61821 | -46.20412 | 2025-08-29 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3153abc1-2c2e-352b-ab00-4613ab772a60 | -13.67885 | -46.90845 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61f7a01b-8ee1-3eeb-abfd-3ffbd95d891e | -12.86295 | -48.10038 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44df8e01-8f85-34a5-b5af-170c3591a67a | -12.86323 | -48.14249 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2bf9d67-ea2e-38dd-8c97-82414596867e | -9.15693 | -65.78778 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d713c892-cdc8-39ab-be33-bfe7fb5d49b6 | -8.24879 | -61.45421 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1cec8ba6-47ae-38c9-a753-340ef174ec5e | -12.83897 | -48.1699 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6043930c-059e-3772-ad92-630386ea884b | -13.40938 | -46.84675 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd6bf02a-ae6c-3e73-8c2a-56ccadeda806 | -13.03477 | -56.88223 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 904a57d7-6d78-369d-b00f-bd840a4efee4 | -13.01479 | -56.92266 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 519704fa-02ce-3eb0-9c87-8771d08e9d4f | -9.9292 | -46.35973 | 2025-08-29 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4edb31a9-9c8c-365b-80ac-8538456c367f | -12.83945 | -48.16607 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 318e735d-b1a0-3019-9843-986e45ac234c | -9.16642 | -60.78244 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b41e08a-8ba1-32ec-b4bf-b63ad642c958 | -12.92261 | -46.34983 | 2025-08-29 05:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 36b36fc4-bea4-358c-800e-1978919d691b | -10.62096 | -54.91086 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 67521529-c839-3f96-b4fe-502d691e52a2 | -8.28879 | -61.40781 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b696ff6-1e3c-34fa-95fd-19a1ba665117 | -14.79508 | -59.7136 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac7e1de1-f950-30f6-b790-7dc92decdbde | -11.72571 | -61.75629 | 2025-08-29 05:08:00 | NPP-375D | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c35bdbf-bbd0-3a54-83c7-35d0072aee3c | -12.83295 | -48.17163 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a5a65fbc-f949-3084-b97a-7742bd8afe3d | -10.48271 | -57.96663 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c529570d-1155-3de9-9820-71d1b18b1ce4 | -8.2834 | -61.41454 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f520f256-1afa-3ec2-8a8f-3dec9638f7d5 | -12.69852 | -48.14717 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5c96fab-d850-39b6-94aa-acac9119f83f | -9.88228 | -64.69249 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96e14783-d863-3b0c-b17a-6063a15a9c22 | -13.01535 | -56.91911 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d324eef-6f2b-342b-9469-09e739e7aef6 | -16.78317 | -49.24985 | 2025-08-29 05:08:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75efb091-1564-3e06-9740-287f4a8c00c4 | -9.21556 | -60.87022 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9905c49-7cd9-35b8-adcb-4589c96842dd | -9.54915 | -65.69581 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48d1fdd0-d4e2-3f29-ae4a-f7ad0bbb3ccc | -13.58298 | -46.86984 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5127a634-6882-3b4c-8700-c281a4c22135 | -9.66859 | -65.03493 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b05eb79-80f1-36fb-9a7f-6d12ff6c5585 | -10.36654 | -57.79572 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52d4a68-661a-3b77-a38c-e3aaa473fdfe | -11.11932 | -45.12297 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README68.md)
