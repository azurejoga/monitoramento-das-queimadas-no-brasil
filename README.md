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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d46e9ff0-657b-3e26-b500-076e4c53c1eb | -9.0832 | -47.9374 | 2025-10-09 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d1e95091-b114-3f2b-8f53-4deaf11c6771 | -19.7553 | -42.1994 | 2025-10-09 00:00:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| 82ea9c4c-1ad3-348e-b9ec-83da9a87f7d8 | -13.8103 | -45.8519 | 2025-10-09 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 189.1 |
| ce2518fd-53c0-3143-a48b-e070e341a160 | -13.0376 | -43.9079 | 2025-10-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d53723bc-e588-3578-8490-850091b197ee | -5.3063 | -45.3635 | 2025-10-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 7f78b8bc-4fc7-31b4-9d76-f116b1403e21 | -5.3249 | -45.3623 | 2025-10-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1f11d165-324f-3ada-a255-60f4563872a0 | -17.6221 | -47.1912 | 2025-10-09 00:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8da4e1ca-f590-3580-bb76-91585095b544 | -19.7347 | -42.2052 | 2025-10-09 00:00:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.5 |
| 6f5da89f-ed29-307b-9b7c-0dafaa2d2ba0 | -14.4133 | -43.9911 | 2025-10-09 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 383.4 |
| cf72f3cb-c303-3d12-8f30-c1fe143249a3 | -4.4632 | -43.2386 | 2025-10-09 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| b77d0541-36c0-360c-83a4-67547cd3fc0a | -10.8745 | -44.6404 | 2025-10-09 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| a59a875b-b608-306c-a9cc-85f5748d0f6d | -10.8749 | -44.6172 | 2025-10-09 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f9e227e5-409b-3dd2-8b3d-891f71d58d65 | -13.8108 | -45.8288 | 2025-10-09 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 77f2206f-c87c-32d9-a8d9-b8f68be13c0a | -18.9974 | -43.0805 | 2025-10-09 00:00:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| e4353da0-7841-3c99-800e-a0978f61b5c7 | -4.4633 | -43.2152 | 2025-10-09 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 02cdf33d-961e-3074-b8fe-fa6a693406ac | -16.3955 | -46.3741 | 2025-10-09 00:00:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ceea3c04-0e91-37d0-9dec-d162a281387a | -10.8505 | -49.9217 | 2025-10-09 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 98e4a504-1653-359f-9d37-d33b8e3db1a2 | -17.8413 | -57.6459 | 2025-10-09 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 9fcce9b3-e125-3fc5-a7e9-710b057b07b2 | -13.7909 | -45.8552 | 2025-10-09 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 324.9 |
| e607fa5a-350b-39c2-90d7-ab03001c51ca | -5.3061 | -45.3861 | 2025-10-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 48ebdb02-0fe7-373a-84ac-802c68c1ace6 | -7.7758 | -44.0164 | 2025-10-09 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 897ec847-ee4d-3aec-af35-664d22f03c67 | -18.0596 | -44.9392 | 2025-10-09 00:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 322e5f00-a598-307a-89e4-4c538dbbc10a | -4.105 | -50.0436 | 2025-10-09 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f41021b7-56f2-39d1-bb8f-b21d487329cf | -7.7567 | -44.0415 | 2025-10-09 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 193.1 |
| e193fbe3-3363-386a-814b-dc18fb56813a | -9.1018 | -47.9575 | 2025-10-09 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| f90eadb9-17b6-3600-9458-51215c4c0b21 | -10.7262 | -49.3317 | 2025-10-09 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0e446d8c-4c20-35e8-b9ac-93e2c08b11a9 | -14.4334 | -43.9635 | 2025-10-09 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 291.2 |
| e29c609a-94e0-321c-a928-286fb8c07d59 | -13.7714 | -45.8584 | 2025-10-09 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| bcd7a224-6522-3452-8a74-8f9f7f30a986 | -5.0401 | -43.5973 | 2025-10-09 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| eeaa9163-53ec-3f37-b0bd-7a39308bf8fc | -13.7904 | -45.8782 | 2025-10-09 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 320ef44b-724c-35d0-a500-45cbe5093b3a | -4.9894 | -45.3159 | 2025-10-09 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 1b3daeeb-2944-3ab2-b3aa-e10a3569ad3d | -4.4446 | -43.2164 | 2025-10-09 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| ae126941-bca2-300c-bff8-1f9167e556c9 | -4.278 | -48.8891 | 2025-10-09 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 41fd0034-6cd1-3c21-8eeb-94951de88a73 | -13.7913 | -45.8321 | 2025-10-09 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 0139a7dd-b67d-350c-9141-52f1c627322c | -4.9708 | -45.317 | 2025-10-09 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ce596235-1707-3971-a36a-51d572dfc77b | -14.4329 | -43.9874 | 2025-10-09 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 205.2 |
| f690a167-265f-3380-8798-84537250fdb2 | -16.0042 | -50.8147 | 2025-10-09 00:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ab417e0e-305c-3fc2-a391-dbc1b468a504 | -11.6451 | -44.2966 | 2025-10-09 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 6fc23533-f9bc-348f-bd1c-19e7bccbb9ce | -4.4445 | -43.2397 | 2025-10-09 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 2b1cc06d-c47a-39d8-bf75-666e125201c3 | -18.4118 | -45.2394 | 2025-10-09 00:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 80afed2e-2921-361a-ab64-93662a4306fc | -4.9896 | -45.2933 | 2025-10-09 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f790a8d6-1fa3-32f4-98b1-4369a001b26e | -5.3248 | -45.3849 | 2025-10-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2ffa197e-2452-3e8c-95f6-6d2f4f4cf2c3 | -9.1021 | -47.9355 | 2025-10-09 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 30bd6072-efd8-3ea8-af25-9b047640c3e2 | -7.7569 | -44.0183 | 2025-10-09 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 77a9331c-2772-3d42-9b31-d4105bec8ad9 | -7.7755 | -44.0396 | 2025-10-09 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 75281e16-c866-3329-8b01-718d1cf61be4 | -14.4138 | -43.9672 | 2025-10-09 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 591.5 |
| dbe2be50-c721-3f35-8942-ccee3a337cec | -9.0829 | -47.9594 | 2025-10-09 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 8f75a901-665c-31a0-96cd-a7e6566629a4 | -9.6866 | -49.3766 | 2025-10-09 00:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 13781aaa-1847-3167-8a57-a03d27065011 | -10.1639 | -64.25 | 2025-10-09 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 83253c7d-b5af-35c7-abfa-c95fba5c93d2 | -15.9846 | -50.8177 | 2025-10-09 00:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 11c66808-35b4-3410-b9cd-3b708b96e72b | -8.1993 | -43.3424 | 2025-10-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 2e9c5692-66f1-34c8-8154-586f2e134f88 | -13.7714 | -45.8584 | 2025-10-09 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9fd76d00-93ef-3d87-932a-c60b44e42138 | -14.4133 | -43.9911 | 2025-10-09 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 262.1 |
| 59e974de-67d8-3ebb-9a46-878b3c889f64 | -13.7904 | -45.8782 | 2025-10-09 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 34313840-ac93-3db9-9cdc-a0d0b0e79dfd | -17.6221 | -47.1912 | 2025-10-09 00:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5b23c5b9-c446-3eea-a983-18f329fcf5f3 | -13.8108 | -45.8288 | 2025-10-09 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| c2fc8d7d-1551-3b08-8624-b5fd0cad28c4 | -6.6995 | -46.2946 | 2025-10-09 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 268.3 |
| 31e361b8-507a-308d-ac59-04c0d7ff781e | -6.6808 | -46.2961 | 2025-10-09 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 317.2 |
| 332829a5-6bb2-3d98-9252-447c4464fd0a | -14.4334 | -43.9635 | 2025-10-09 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 640.8 |
| 6c66217b-c32f-3a6c-93d8-8394602b396f | -13.7913 | -45.8321 | 2025-10-09 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 57588c0d-fe34-3ea6-93fd-96c10145c54d | -4.4632 | -43.2386 | 2025-10-09 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3f6a5ce5-06b9-331f-8ac7-766c5a16441d | -9.0832 | -47.9374 | 2025-10-09 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 145a409c-ae8f-32c8-ae45-4ca80e1b94cd | -7.7755 | -44.0396 | 2025-10-09 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| ba013502-7bed-3bf9-b7f7-5d0f721782ae | -7.7758 | -44.0164 | 2025-10-09 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 3c1855ed-e252-30ab-874b-1d1023ab543e | -14.4713 | -52.9148 | 2025-10-09 00:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| fbe0f7cf-29aa-31a2-9e9c-b3b96e252875 | -10.1453 | -64.2508 | 2025-10-09 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3f7d173e-a6b1-32be-9c7a-2f59b6cf6bcc | -5.3248 | -45.3849 | 2025-10-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cce586c3-2a30-36e1-a492-8050528bfe33 | -10.8558 | -44.6199 | 2025-10-09 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1c7aab44-4fb8-3229-9dc6-c96f50809918 | -10.8554 | -44.6431 | 2025-10-09 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 56faae7f-8bf4-3d95-b075-d6254b3433e8 | -4.2781 | -48.8677 | 2025-10-09 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9aa802a9-e400-3397-8f65-f3610285ce8f | -19.7347 | -42.2052 | 2025-10-09 00:10:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 4fea2e66-eee4-3596-9a0f-e7cccb9c0a43 | -5.7979 | -44.6715 | 2025-10-09 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| da239dd9-bdb2-3d91-8e46-3144aef89c80 | -6.6993 | -46.3169 | 2025-10-09 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| f747b74a-bceb-35d3-88a3-372181b3e66b | -3.0979 | -47.7938 | 2025-10-09 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f3ca6944-2b8e-39f2-84ec-08389ee289ae | -17.8413 | -57.6459 | 2025-10-09 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 8007a033-56d6-3bfe-8a56-6f2cf2701552 | -4.9709 | -45.2945 | 2025-10-09 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 36965ae8-6de0-3193-b875-9a7b24fb2862 | -6.6806 | -46.3184 | 2025-10-09 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 34b496e2-8a74-3176-9c26-5dc304850f98 | -4.9894 | -45.3159 | 2025-10-09 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 37c232fa-b34e-3d69-a7ab-b9a88775bd51 | -5.4415 | -44.8107 | 2025-10-09 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 9381a8fe-5b9a-3284-9a71-74cad19f4604 | -13.8103 | -45.8519 | 2025-10-09 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 81e0e8ae-90a9-35f2-bc05-f5199732c5cf | -14.4138 | -43.9672 | 2025-10-09 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 507.9 |
| b228f4de-c122-3814-b909-362ed06479c3 | -5.7981 | -44.6487 | 2025-10-09 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2686fd05-9dac-3c73-97d1-47f7c0f97ef7 | -14.4329 | -43.9874 | 2025-10-09 00:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 318.3 |
| 4162f9b1-df69-3615-8219-403e783cc592 | -9.0829 | -47.9594 | 2025-10-09 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 323069c7-fa61-3b7b-9784-d97f4b83920b | -4.4633 | -43.2152 | 2025-10-09 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0dac3760-06b8-326a-bf09-15225b5ae55b | -4.9708 | -45.317 | 2025-10-09 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 54752e26-b61c-3734-a81d-45de690c48af | -17.6421 | -47.1871 | 2025-10-09 00:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9988bcb8-9e35-33c3-a258-13fdb4c50dc4 | -8.1993 | -43.3424 | 2025-10-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| d89df13c-02e4-3c9d-9c69-13978ebec0af | -13.7909 | -45.8552 | 2025-10-09 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 359.9 |
| 4028e632-2047-3a0c-abba-756f564642a7 | -5.4413 | -44.8335 | 2025-10-09 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3228e1bd-1597-3a35-bba1-b4935ac948aa | -5.3063 | -45.3635 | 2025-10-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7a9f156c-92eb-34b3-87b8-56d1bf02d3ec | -4.4446 | -43.2164 | 2025-10-09 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ed855b7a-1775-334c-ade7-e755519ccf3d | -4.4445 | -43.2397 | 2025-10-09 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 053edefb-e1ea-3cca-b71a-9c1b42932589 | -9.1018 | -47.9575 | 2025-10-09 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 4cabbfb3-72ef-3100-834c-2f3258fad222 | -7.4018 | -34.9979 | 2025-10-09 00:10:00 | GOES-19 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| e5988a4f-2ced-32a5-a7c3-3c4f4f96ccb9 | -7.7569 | -44.0183 | 2025-10-09 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 69a43fd0-e714-35e0-9f18-b616f6198902 | -15.4772 | -47.9578 | 2025-10-09 00:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7e8a9173-fd65-303f-8d2c-63d61fd6ba8b | -19.7553 | -42.1994 | 2025-10-09 00:10:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 43c01b21-32bc-350e-a7aa-27cb05fe1110 | -4.9896 | -45.2933 | 2025-10-09 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| beeb4a2f-733b-3293-a9a2-53584fd2cf80 | -5.3249 | -45.3623 | 2025-10-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |


[Clique aqui para ver as próximas entradas](README2.md)
