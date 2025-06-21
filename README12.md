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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d34bf20-45c2-3197-869d-72fcbd87de88 | -11.53503 | -56.96815 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 988f6f0d-757d-36d2-af62-508fff5302ce | -9.01786 | -61.23656 | 2025-06-21 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9521cd47-44f3-36e1-b35b-42e912459c98 | -10.52357 | -47.58165 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2eb3d1c-5ce0-35c5-ac0e-507d235dfb3d | -11.79757 | -49.52211 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ab2b86-5d49-309d-967a-658cbb9c0d58 | -12.16211 | -48.68837 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee69c2d2-01d1-305b-91f5-93e316f9f577 | -7.9431 | -48.03925 | 2025-06-21 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 014d9730-c6f9-34a0-aecf-0d3b90300aab | -11.95036 | -58.74343 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae4c5dd1-40fe-351e-9365-e4cc5e7ff407 | -9.60021 | -56.28547 | 2025-06-21 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e06ee2-711e-35dd-b0e4-0ec8f0db8653 | -7.87445 | -47.89009 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c14f4598-f8dc-30c3-a4c2-7a2efabcc5fa | -12.26078 | -44.60307 | 2025-06-21 04:34:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ad90c89-8634-332a-bd61-55b26f134c53 | -10.50735 | -47.57544 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b2dd02-3db8-3d1f-bf2b-7a2005f3d8f4 | -8.70457 | -50.05043 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09c29d46-4f76-3edc-ac54-bada25ae188f | -13.0403 | -53.71593 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| af4b8441-946e-36c6-8afe-0e192d1bc4d3 | -11.21122 | -47.83907 | 2025-06-21 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 95d61b46-576a-334c-96f5-3ac494d12f7a | -12.57301 | -58.38282 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccec4505-fbba-345c-8e12-03795c2a778a | -10.46282 | -47.03709 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dae6d9d3-cbec-3288-a46f-2d2b437eaee3 | -12.63587 | -44.32832 | 2025-06-21 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b56453a-c38a-3f9d-9dbe-c22b5f8ce35c | -13.03651 | -53.71525 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ed27219c-ba74-3e8a-b163-90582ccd3bfd | -12.28329 | -50.1079 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af8668dc-c81a-32e0-bb1c-e4ae2075f681 | -11.83302 | -57.75872 | 2025-06-21 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82534455-6ae9-36ab-9f19-d6750047fa86 | -10.51686 | -47.5806 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed02f7ba-4a71-3843-ae0a-5db941471ce3 | -12.47741 | -60.14173 | 2025-06-21 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dd5fc3e6-c963-3dfc-99e0-24ca6b6d1e4c | -12.57089 | -58.36586 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 849094de-12c1-319f-9978-6ce4b1157a5f | -9.91749 | -52.44714 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 169e8717-0f7f-354b-b736-e5c4aeddf51d | -13.39126 | -48.45234 | 2025-06-21 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ed5abe2-4e78-3597-a358-4a87d53d65af | -9.47454 | -57.84827 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ae32892-7882-3826-8d47-6e04902b5156 | -9.48036 | -57.82079 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 258d5ac9-acd3-345b-8983-9c6b6adb0661 | -12.50739 | -58.35447 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3ca3427-96b3-32a4-8b6b-c78bc6458dd7 | -8.02183 | -47.66371 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39490501-987f-3cff-9bcb-1a75f331075e | -12.16157 | -48.69191 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 688b149b-bcdb-3b69-bde1-585785012262 | -11.88194 | -54.66777 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 46a4378d-acc1-3fc1-bddd-9a5b54419045 | -10.50906 | -47.58675 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f0aec3-b3e7-32f2-b4bb-6e1a823d1a7f | -9.4751 | -57.81978 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41b585ef-6dd9-3c80-b059-2ab9ff9d15ea | -11.25954 | -52.46491 | 2025-06-21 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45477407-df42-3130-8e48-84214e782e67 | -13.36427 | -54.25724 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d099942b-7de2-304c-94d1-6839a680ac51 | -14.22637 | -45.51451 | 2025-06-21 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c15c73d-71df-31a2-9079-6d5ba89a77b9 | -9.47676 | -57.84082 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 566812df-fbdb-3787-b68a-1d8844491257 | -13.25864 | -46.82959 | 2025-06-21 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3932d69-e7d1-3533-97e9-3bd914bc9ffa | -13.89347 | -54.62244 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b1db904-8d7a-3d52-bfb5-cc4ff18a29bc | -10.95487 | -49.25565 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49c0e485-c982-3efc-ac69-056edbd65807 | -9.47391 | -57.8516 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2db5c30-ce6d-3fba-a810-bb2975265c2d | -13.1446 | -56.80525 | 2025-06-21 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f1d9d4a-04fc-3c33-b6e5-ee9df4df8a84 | -9.47702 | -57.83501 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4e7ed22-34c1-3a25-a867-c07fc506ac9e | -8.18159 | -47.77481 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f59b62e-042a-3c83-8d55-d79d0612375b | -9.12088 | -49.66102 | 2025-06-21 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f00bba8-53f2-38ad-9a5b-d72780b8553b | -8.38235 | -46.97614 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed88d630-586d-3ba1-815b-e52cd08a736c | -12.47661 | -54.42332 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7a598354-8291-38e3-b31b-24c099f0238c | -11.93744 | -48.42469 | 2025-06-21 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3663a923-9061-3f7a-bcd7-9b196d94987c | -8.73363 | -47.98681 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db307ada-908b-3979-be35-cb43bcfd0905 | -8.98573 | -49.86939 | 2025-06-21 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e27044d2-ee8a-3455-9803-834cc3e61477 | -10.86736 | -53.76236 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bc72d47-b06b-3bac-a285-7aa4605454c4 | -10.15637 | -48.98728 | 2025-06-21 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47a37256-93dc-3af4-8dc9-df1627b91a75 | -8.38181 | -46.97975 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae572f23-4ebe-32b8-8627-7d50651e5a3d | -11.94837 | -58.75374 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5da03d67-e416-3dba-aba5-596b7063dd80 | -10.83245 | -49.6635 | 2025-06-21 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f2e036a-0fc6-355e-824b-d6874a741936 | -13.14285 | -56.80879 | 2025-06-21 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64c7a69-85c0-3cec-81d8-4656e49ffb0d | -7.87775 | -47.89061 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ed28cc4-9265-300d-89a5-e8ccd301bbde | -8.37281 | -46.97096 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f674dc-4dad-3b04-9ae0-fdaaf3eb0a71 | -10.44809 | -47.0424 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 548bf263-5e21-363a-aa47-e23c2fdee9e5 | -11.87719 | -54.67077 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| b150ebeb-392c-3aaf-96dc-1c8329ff2b29 | -12.97324 | -54.68151 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa54c97f-bb1c-3d01-b053-810c03ead462 | -12.476 | -54.4269 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3a4780b8-4d17-38f5-81a2-99b437d12be3 | -9.47616 | -57.84415 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7211fe39-fdf3-337b-ad52-5b5aed8fb20b | -8.19098 | -47.77984 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a1e7e70f-f0d8-387d-88da-58ecab76dafd | -12.47262 | -54.4226 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f6dc6e2d-8c82-3883-a93c-8295810a8896 | -12.4276 | -54.87101 | 2025-06-21 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d677b0e7-07fe-3ed3-bac3-46ae302ca160 | -14.22572 | -45.51935 | 2025-06-21 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca8f9565-173f-3875-af29-a50a5ef4e350 | -12.57994 | -56.98418 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e7d2abc-57a1-3498-a8ac-04ed05c55203 | -9.7376 | -48.33495 | 2025-06-21 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d50cdce4-fff9-3fd2-9340-8577a04ec7bd | -9.46685 | -57.8353 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19b89f23-556f-360a-9405-3f28d43ba311 | -14.30933 | -49.94879 | 2025-06-21 04:34:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b24e8664-581a-3772-9beb-717689285286 | -8.19591 | -47.7699 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2c4354f-1431-386c-8022-6efaec8af7f0 | -10.15307 | -48.98676 | 2025-06-21 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 677f019a-92e9-392b-b63f-6f12f90b3bb5 | -13.36812 | -54.26024 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d494a77-89a4-3a76-a5b8-df3c4d294d52 | -10.44468 | -47.04186 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f19cb46f-bf9a-3b43-963a-1bf38131bfc0 | -12.29049 | -50.10544 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 192bef18-8a27-38a7-8e9d-20086835996f | -12.47373 | -54.42656 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 255d0978-ae05-3833-b660-989367e18d49 | -13.09993 | -52.29697 | 2025-06-21 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db3ec31-eaba-33fc-990c-caa740186769 | -12.47437 | -54.42299 | 2025-06-21 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 705fea24-e9dc-3e6f-a1d1-5c9aabc47953 | -12.52215 | -57.21165 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1dbd6b64-f111-3e4d-be5f-1f922b44b1d8 | -8.1849 | -47.77532 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38ea24f9-e86d-3d30-9816-5e4816db95d9 | -9.47117 | -57.83715 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc202e8f-cead-3ec0-968f-5fffbe76ecf5 | -10.10061 | -47.23094 | 2025-06-21 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 948ecfed-7f7a-3224-909b-aed6a4106549 | -8.02291 | -47.65674 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27185a62-3783-36d7-9ebb-28156f8bbc74 | -11.79097 | -57.23742 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 657848ef-42eb-3e2b-9f0a-8c175c2b04bc | -10.46338 | -47.03336 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02cd3e56-c083-320a-bbff-d3f8919f2f88 | -11.8375 | -57.76263 | 2025-06-21 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a452e739-d2fd-3f62-9f91-828df5a972d9 | -12.22435 | -49.64222 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a3f9250-feee-37ab-af87-e1ab881c9203 | -6.53255 | -55.02128 | 2025-06-21 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff3a5be-ea8d-387c-bb2c-705567a10999 | -13.30771 | -46.42093 | 2025-06-21 04:34:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af5e3420-47f3-3021-8546-faa5467cfbec | -12.50821 | -58.35727 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 68f199ac-3601-358f-aa18-0bc6047a1be9 | -12.52283 | -57.20995 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d9f6e4d3-547a-338f-9d20-8ad08bfb1468 | -11.8677 | -54.67677 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6a808317-43ca-3214-911e-44f2056b648d | -14.49971 | -48.00517 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8632faea-869c-3f42-b411-14c98aa9792b | -11.13917 | -53.92078 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 398eec86-12ba-3acd-93a1-0a195a95c6fc | -9.02595 | -61.22196 | 2025-06-21 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3297011d-e630-3b57-80c2-97921ea0507b | -10.14922 | -48.98972 | 2025-06-21 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5723ec59-0372-3c47-a12c-1611dee4c7e1 | -9.47301 | -57.82732 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 257c2cc9-aa2b-36ad-a81a-e58735dea1e9 | -11.94164 | -58.75983 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a584d9c9-718a-373c-9509-4ce5120aceec | -10.86631 | -54.31797 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
