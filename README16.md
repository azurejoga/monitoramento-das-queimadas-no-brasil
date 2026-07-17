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
| f8d53a4a-24c8-3ee2-bf7a-7ec271d6a896 | -9.91341 | -53.32806 | 2026-07-17 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2253ce3d-e26e-3df1-96af-0319b1f0224d | -12.41556 | -58.39983 | 2026-07-17 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bd5a417-10e6-3a58-83fd-5f07955e0ec8 | -9.91749 | -65.00253 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6b98d64-574b-3b28-9f91-64c1bb2702ae | -9.46471 | -64.04079 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf2187fc-21fa-3d2a-9d3b-a50ceb566289 | -9.45501 | -64.03556 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 339b9532-b3c6-31d7-bb57-fefee583b1f2 | -9.45788 | -64.03979 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 10db0420-9220-3dbd-b5a4-719ca1adb3a9 | -9.46129 | -64.0403 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5bc0fc1-d6b8-3b3a-92fb-e75a6aacf72d | -8.60566 | -63.46131 | 2026-07-17 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 354f7d69-0398-399a-9c89-25fd4d7bf9e4 | -10.46891 | -62.45002 | 2026-07-17 05:44:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb694d6f-c398-3fa1-8a16-31c8847c5f26 | -9.45446 | -64.03926 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 935eab52-7e55-3071-9ed4-748d75e0be72 | -9.91694 | -65.00609 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa17584d-ec8f-3448-8ceb-41a829045423 | -9.46242 | -64.0328 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c468d103-81b8-3d7e-b8ba-54cfb642f03f | -18.56282 | -56.82127 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| be0b2892-99c4-397a-917b-c1f766d3da2c | -18.55686 | -56.82059 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 70c0dc4b-bbee-32dc-b3d2-149ba55220db | -19.85452 | -57.98675 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 07b17304-7571-3eec-91a8-ec0fd0a255e3 | -21.66259 | -56.33191 | 2026-07-17 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed94737e-ae33-353c-8f2b-19a382f4f297 | -19.85244 | -57.98389 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8c41bd7c-1374-37b3-ac32-c4bc396005f7 | -19.85975 | -57.99139 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6fe20a5a-ff25-3fff-ba4d-eb0cab82033c | -19.81782 | -57.95411 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6a2cc46b-24e3-3a44-97d7-f31f7f58e5af | -19.83802 | -57.98077 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 74567609-96a5-3d9e-94ef-4e8126d89653 | -21.77019 | -56.29906 | 2026-07-17 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a350dae4-a11e-352e-88dc-fb0c1eb89fa2 | -21.66301 | -56.32669 | 2026-07-17 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 061ccda7-b9da-3cb4-9290-bee0911c4293 | -21.76975 | -56.30449 | 2026-07-17 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 444bcd2e-c218-31d6-a44b-5f6f07bf6f30 | -19.84196 | -57.94071 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8e33933-a0ea-3cd1-8bee-6a9628229dd7 | -18.55729 | -56.81603 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e94b5df9-bb9c-31ba-b737-26055f3a1ac0 | -19.86538 | -57.99205 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dcf89cff-ba09-3089-976c-5ae82580e3e7 | -19.81743 | -57.95813 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ecf54055-4dec-35d5-bfd2-602c7e31c2db | -19.82715 | -57.97547 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 05953f3d-60f2-319e-948a-50a9a159c906 | -19.81665 | -57.96615 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 26749065-571b-392d-afb7-421d9d875502 | -22.23589 | -56.05045 | 2026-07-17 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6396b4b1-7f2f-3119-8409-93b53cfbc1d0 | -19.8577 | -57.98857 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f040fee-ca67-384e-ac82-3f499d0ae1c6 | -21.76338 | -56.30386 | 2026-07-17 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e7e91ca-af68-37ce-9adb-912221aad62a | -19.82463 | -57.94273 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0564b8fa-59f9-31de-9a53-4626298ad00e | -21.76381 | -56.29849 | 2026-07-17 05:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6ba0e26-1f13-35df-abd6-7cb9ea1ac472 | -19.84889 | -57.98609 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 31539ec9-e25a-382d-be52-91f0cbb48567 | -19.8186 | -57.94609 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0b75efc2-b062-3630-9ec5-3fc9e3f7563c | -22.24242 | -56.05061 | 2026-07-17 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df16dabf-1c05-3589-823e-d51887585c47 | -19.84365 | -57.98143 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d5f84c07-d52b-3cf2-b44d-8f72c06d1d24 | -19.83027 | -57.9434 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 421c0d79-047f-313d-9467-a5b8cdb78df9 | -22.24202 | -56.05197 | 2026-07-17 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de1a600a-0eb5-3da3-bb23-cea8e546aff1 | -19.82151 | -57.9748 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2a02c990-fbe7-35a5-a614-0e861bb6602d | -19.83631 | -57.94006 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 33f3d0c7-0cf0-3ee5-b748-cae3202895e9 | -19.81705 | -57.96214 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c8abb719-797a-330f-8cad-e84f3ef15f02 | -19.85207 | -57.98789 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a7fa3d7b-6d86-335e-bcd0-925175406e69 | -19.83067 | -57.93937 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e19e59a5-d4bd-3e96-adae-9cea8bb1d4b7 | -22.23549 | -56.05186 | 2026-07-17 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 188e2a61-13af-3cf7-8484-adb15c6299c0 | -19.83278 | -57.97613 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 81a54977-1c9a-36fb-b385-0f76eef88e1e | -19.8219 | -57.97081 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c216e443-fc26-348c-843f-6bdabaec837e | -19.82424 | -57.94675 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9669a36e-9055-35a5-9578-1425c6b4eabe | -19.86334 | -57.98924 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d717f8ab-5d66-3a16-ac56-37796ac0c78c | -22.21918 | -56.10147 | 2026-07-17 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eef5ace2-114f-3708-871a-d38401894e13 | -19.82502 | -57.93871 | 2026-07-17 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 31f936db-c442-32f0-9cf7-b0564bb44fae | -13.2456 | -45.0909 | 2026-07-17 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 122f2808-c9d1-3469-93c9-22bceed7d93a | -12.6983 | -46.508 | 2026-07-17 05:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e2625239-c90e-35e2-b5f0-1f5c9d946bdc | -13.2649 | -45.0877 | 2026-07-17 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 8aab0913-c9c5-3f96-b18f-3181462a6ddf | -13.2645 | -45.111 | 2026-07-17 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 3588426c-24ec-3d72-a5f9-9f9ee368d1f9 | -13.2451 | -45.1142 | 2026-07-17 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 6d787edc-db72-3bbc-b7e8-2fa4a92f8acb | -13.2645 | -45.111 | 2026-07-17 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 4d6c2a4e-3e7b-3a0c-9d03-e13d3a010b1c | -13.2451 | -45.1142 | 2026-07-17 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| ec44b126-e307-35b9-82ef-9d3d76aa5ec8 | -13.2649 | -45.0877 | 2026-07-17 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 45b94959-1ffc-32a2-a5ec-b7fadb6aa4af | -13.2456 | -45.0909 | 2026-07-17 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| a3b60561-bde2-3f36-ad0e-f82b1de136fd | -13.2649 | -45.0877 | 2026-07-17 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| a98a3509-6c4e-36b5-88ee-e625c01ec926 | -13.2645 | -45.111 | 2026-07-17 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 6b2ae608-0db2-378c-8358-aa89cb495a2c | -13.2456 | -45.0909 | 2026-07-17 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 229.4 |
| b9eddcec-0372-399e-b2ad-b3d6fa31c57d | -13.2451 | -45.1142 | 2026-07-17 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| e1de5fc7-5a16-3e7e-ae17-93c05e083af6 | -13.24 | -45.13 | 2026-07-17 06:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8593ec5-1b03-3cac-8ea7-f2ec792fb87c | -13.24 | -45.08 | 2026-07-17 06:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 252e918e-20e2-3ac0-a8ec-1d3d60caea55 | -13.2649 | -45.0877 | 2026-07-17 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| c85ad8b5-31dd-33ed-a580-c1d550b96450 | -13.2451 | -45.1142 | 2026-07-17 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 64fa3654-6ed4-3160-ba3d-d2c33e2575cf | -13.2645 | -45.111 | 2026-07-17 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 72c7e183-49a3-3df2-b168-d2ecda19bbb0 | -13.2456 | -45.0909 | 2026-07-17 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 2d087110-a95b-34f9-8f5b-22b264c0a052 | -9.45662 | -64.04076 | 2026-07-17 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8c63cd4-a40a-35ae-bbd2-35080b584d76 | -9.45701 | -64.0379 | 2026-07-17 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eb819f4-18cf-3228-a77c-ffd36d7d7d69 | -9.46175 | -64.04144 | 2026-07-17 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 186f4617-0a6d-3271-b287-e3d42a14c774 | -9.45625 | -64.04357 | 2026-07-17 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90ed079d-0e7e-3784-a28a-afd6a8c3b82e | -9.45189 | -64.03712 | 2026-07-17 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f287bca-0ad9-347c-991d-301ed1d39c01 | -9.45152 | -64.03993 | 2026-07-17 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 451e1cc5-8712-3097-b5d6-100e900a8430 | -13.2456 | -45.0909 | 2026-07-17 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 271.9 |
| e49c7fb1-25a3-38a2-85f4-7cf881263ef2 | -13.2645 | -45.111 | 2026-07-17 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 767dada9-8d84-3a2e-8a6a-a850424e79ca | -13.2451 | -45.1142 | 2026-07-17 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 8b159ebd-c9a7-3731-94df-921eb8d7ad76 | -13.2649 | -45.0877 | 2026-07-17 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 8ba70116-3661-39bf-ad55-c8662d8b246c | -13.2645 | -45.111 | 2026-07-17 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 4deb5443-da71-3ccf-98f0-a49d81a6beed | -13.2456 | -45.0909 | 2026-07-17 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| c03479ab-4231-3739-aeaa-c3c93f340c09 | -13.2451 | -45.1142 | 2026-07-17 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 650f765d-4f79-391a-af76-ec3aa6c1f0b1 | -13.2649 | -45.0877 | 2026-07-17 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 219c23e0-9c92-3137-99f6-525ae626cb96 | -13.2645 | -45.111 | 2026-07-17 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ee11bd7b-c442-3dcd-b810-97d33db269dd | -13.2649 | -45.0877 | 2026-07-17 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 7239404a-8aac-37bc-8d9f-412eb2e721f8 | -13.2451 | -45.1142 | 2026-07-17 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| f6dea2bd-4d2d-34e2-8452-0a5e1e5c87ac | -13.2456 | -45.0909 | 2026-07-17 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| bcd7fb31-b1c9-35ca-9076-eaa15ff8e983 | -13.2451 | -45.1142 | 2026-07-17 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| ce62f7d2-37e5-3edc-8c93-c2900aa2f032 | -13.2649 | -45.0877 | 2026-07-17 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a8fcb3eb-f0ee-3407-8e45-1053a1c2f937 | -13.2456 | -45.0909 | 2026-07-17 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| cd73bf63-a482-3072-b00c-0e0545e9e175 | -13.2645 | -45.111 | 2026-07-17 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ddca277b-bfd5-37c4-92ac-d099c17d32f7 | -13.2649 | -45.0877 | 2026-07-17 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c48a285b-0400-3a25-b1fb-c5ad7d360b51 | -13.2645 | -45.111 | 2026-07-17 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1dbaab10-db96-3201-93fe-c35618f26839 | -13.2451 | -45.1142 | 2026-07-17 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4d1389dd-17ab-374b-892e-ff2b3aaf5fba | -13.2456 | -45.0909 | 2026-07-17 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 6ae268af-874f-383a-a279-aa457ab5613d | -13.2451 | -45.1142 | 2026-07-17 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ccbcc2d9-10f5-3722-8736-7d7a9e13e240 | -13.2649 | -45.0877 | 2026-07-17 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| adfc23c0-bf76-3013-86b8-1077661c9878 | -13.2645 | -45.111 | 2026-07-17 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |


[Clique aqui para ver as próximas entradas](README17.md)
