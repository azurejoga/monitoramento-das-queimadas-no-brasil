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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5264a91-e427-31f4-a65a-f2cf7bb5cb6a | -7.8443 | -61.1413 | 2026-09-01 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dcd87fef-391e-38ba-ad03-6d25adce74f0 | -8.5214 | -54.8814 | 2026-09-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 03896a7b-2bb9-35f1-940a-6d65f778642a | -10.6769 | -46.267 | 2026-09-01 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0b2d4717-197a-31e0-82d3-e1fedbaba7b1 | -7.3487 | -60.5883 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 0071709d-dac6-346f-b9ff-2c65ba070b06 | -10.3388 | -49.9977 | 2026-09-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| fb560fd2-a8c9-3ef4-aad6-bbabe69020b2 | -9.4535 | -45.6455 | 2026-09-01 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b5141ba7-20bd-3c3f-a87b-da29352762a6 | -7.9988 | -44.2711 | 2026-09-01 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3552bf12-d745-3766-9fe5-956fb80a98c7 | -7.1167 | -45.7898 | 2026-09-01 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 5fcfc845-f454-3036-b527-4a97ad61480d | -17.1345 | -46.8516 | 2026-09-01 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 15cd8d87-f42a-3a78-98b2-31e327b5640a | -11.2292 | -51.2879 | 2026-09-01 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| cc7a7105-80bf-3279-8098-1a35daa7bccf | -7.8628 | -61.1405 | 2026-09-01 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 827fca34-9957-3a6a-a275-be33f299f9fd | -13.4519 | -57.039 | 2026-09-01 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a6cf2f3d-c979-3c90-9256-f7bb64cdaa86 | -3.1083 | -61.238 | 2026-09-01 13:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c6a2324b-5d9c-3451-8bf7-906903851326 | -6.6542 | -59.426 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b0511a58-8dad-3fb2-80ed-76d79655d4ac | -7.3488 | -60.5691 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 45be22f4-f8c0-3917-ae86-be12d0ff4e2b | -13.9477 | -54.3971 | 2026-09-01 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| d7cf808b-90b7-3069-a959-a5fb98b569fb | -8.7819 | -46.4399 | 2026-09-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 40b9f3ee-2824-33fa-9e83-2e9692ba2a31 | -15.4235 | -52.6836 | 2026-09-01 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| ad6e2d8e-3944-31e5-a8d8-4ff4307e41a5 | -3.6216 | -60.547 | 2026-09-01 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 4cea7e03-ab30-3643-9a1f-9d8d9c8e43d1 | -10.0101 | -46.4386 | 2026-09-01 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| e2e7d68e-ab78-33bf-9a6a-d1db3ecf13d3 | -10.696 | -46.2646 | 2026-09-01 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 277.7 |
| 9f1f6e9c-315a-30fa-ab95-525ba384cf0f | -11.2295 | -51.2667 | 2026-09-01 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 0ccc87fc-ae4c-3c8a-a3de-81819b5a3211 | -7.1786 | -55.4837 | 2026-09-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e6c63b8a-9666-3365-b0d6-eb7890531d2b | -14.6732 | -53.5408 | 2026-09-01 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 918666af-4f7f-3c13-aac3-750750367822 | -8.2602 | -54.9388 | 2026-09-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 197.8 |
| b767b91f-9654-3510-8997-40690dc2983b | -12.9032 | -45.8382 | 2026-09-01 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 95d59faf-526d-3b0c-b477-091470660901 | -7.2006 | -60.6706 | 2026-09-01 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f1f73edf-f01a-30f2-90fb-6e9dfcfbbd45 | -3.5161 | -59.0597 | 2026-09-01 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a2b437cb-f0f6-32cd-8812-e5d5f2bfae28 | -3.8792 | -44.0346 | 2026-09-01 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 42287b42-8631-3382-ae63-c6c348940ea4 | -8.7817 | -46.4623 | 2026-09-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 6595ee0d-43c1-3cc5-a432-6290f9666948 | -14.6728 | -53.5618 | 2026-09-01 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| af5f17fe-9b80-3076-80c9-55550352ecef | -14.7112 | -53.578 | 2026-09-01 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 71aed46b-a3bb-39cf-a96b-83627e61f747 | -15.4429 | -52.681 | 2026-09-01 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 8614222b-15cf-3dd8-b4f9-ecbea2ef62ef | -9.9912 | -46.4409 | 2026-09-01 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a167f173-fdd3-3132-8b58-f0b3774fa1ce | -10.8046 | -50.5046 | 2026-09-01 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 527de52c-1722-366f-95b5-9f791cdf0624 | -10.8627 | -45.356 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 8c6d128d-b8ae-3713-acd0-d8a3d20c95a1 | -12.9589 | -45.944 | 2026-09-01 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8f164c4c-a276-3c58-8df1-804b02787614 | -6.6727 | -59.4252 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8ce0b116-a0e3-3b7f-b701-c7cbf4a81fd1 | -3.1265 | -61.2377 | 2026-09-01 13:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 1e1932e8-0bda-3bd8-ba65-cd3214f79d3d | -6.9552 | -55.635 | 2026-09-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| c924112b-8456-3407-929c-f98be356bf30 | -11.2298 | -51.2456 | 2026-09-01 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c36b7250-4ff2-31db-ac90-8802073365a2 | -14.6535 | -53.5642 | 2026-09-01 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 225973e2-e8b5-323c-a880-227258a6f52d | -11.5479 | -45.4676 | 2026-09-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a5147bc4-a2cb-3810-8bfb-fdb84c96f2be | -10.3391 | -49.9762 | 2026-09-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 14b690f8-24cf-3c61-ad53-e464e145863e | -3.879 | -44.0576 | 2026-09-01 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 270.6 |
| 03aee940-967d-3bad-89dc-d851ef7c684f | -10.3574 | -50.0171 | 2026-09-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |
| b93713e3-ed7a-35ba-a79f-d1beaaec72e4 | -6.1659 | -57.7403 | 2026-09-01 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a2f3a47e-5146-3914-8df1-1f10089f1f75 | -14.5214 | -52.2313 | 2026-09-01 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bf86b51b-d44c-33db-b00b-3c16c1aaae7b | -3.6215 | -60.566 | 2026-09-01 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4ed23a61-6b47-3126-8946-c5fe99a54320 | -15.1827 | -46.2336 | 2026-09-01 13:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 04a33d98-7eac-3a49-a397-2f0fe792877a | -10.8818 | -45.3534 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 353.1 |
| dd7dd470-b53e-378b-9b3f-7951addb354c | -11.213 | -46.0839 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 8953ef2d-3866-3110-9651-88b4df218e2c | -9.4606 | -67.4531 | 2026-09-01 13:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 58dfcb67-2c94-303d-bb82-9002b8d15a63 | -6.8009 | -59.5742 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 9d2941c4-916c-3b4f-87cc-d3f1e8dc53a8 | -6.9553 | -55.6151 | 2026-09-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 48d93ecf-3692-3afa-b712-c113b01d0b88 | -11.2482 | -45.1194 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 41d6cfb9-0eee-398e-9386-3a2a04e533ec | -14.4587 | -52.5151 | 2026-09-01 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 23c98ed0-0220-3e32-a118-86b15e98a5b3 | -9.4349 | -45.625 | 2026-09-01 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 243.4 |
| f5a5bcec-655e-3deb-90b2-d3ef11af51a5 | -6.8036 | -59.0921 | 2026-09-01 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 210d07e3-7806-37f2-b3c8-df0b678c66e6 | -8.9242 | -63.2804 | 2026-09-01 13:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f95b261a-52a5-39a6-87d0-4369823833a8 | -14.6538 | -53.5433 | 2026-09-01 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 66566a7c-5334-3339-ac4c-54ac836ab101 | -10.7407 | -54.0401 | 2026-09-01 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 518cac83-30c5-39bc-9ae7-f36567b9ec05 | -13.967 | -54.395 | 2026-09-01 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 15500f78-b003-32fc-bbad-d1933e9371de | -10.3385 | -50.0191 | 2026-09-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7f20921b-abe1-3a5a-abdc-632fedd898dc | -8.5785 | -54.7566 | 2026-09-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b32558f1-1f37-3fce-9247-70a3306f2d77 | -9.9931 | -46.3057 | 2026-09-01 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1f881404-4017-32c1-98ea-5392e19c5581 | -17.1146 | -46.8556 | 2026-09-01 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7f869762-f8a1-3778-9644-c3bd3d979255 | -10.8407 | -50.6286 | 2026-09-01 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4e3721bc-09f7-381d-af76-c9605f63f781 | -6.6036 | -58.5972 | 2026-09-01 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 58ece3fb-508c-3952-9fbe-e709ced9faaf | -10.036 | -44.7056 | 2026-09-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4c56c9f0-5f1d-3b61-a4b1-d699447f1b07 | -3.9221 | -43.1291 | 2026-09-01 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c3c14f0f-c511-37b8-b4a3-e9bb4c51f595 | -10.7856 | -50.5066 | 2026-09-01 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 214.1 |
| f72e8c9c-d452-3bc0-b7a0-59d885ae7d31 | -8.4046 | -44.9869 | 2026-09-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3ca292d0-55e1-3049-9b87-9ef06da7883a | -7.4153 | -44.2599 | 2026-09-01 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a0583b33-9e92-336a-84a4-d3f5bb030ba1 | -8.4235 | -44.9849 | 2026-09-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c841a8ad-7acd-3e62-bc95-f3dae585c434 | -10.6964 | -46.242 | 2026-09-01 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 75cbc377-818d-3481-a449-48ef1c231261 | -3.1266 | -61.2188 | 2026-09-01 13:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b318d695-2396-340e-ae4c-f43fa5776156 | -11.2478 | -45.1425 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| dff17abb-b4a4-33f4-a791-74145b6fa11a | -14.478 | -52.5126 | 2026-09-01 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b55e1160-8e14-3137-9385-61f7eeaed83b | -10.8624 | -45.3789 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 11ff089a-c8a2-3463-b112-13c2d70aa260 | -11.2673 | -45.1167 | 2026-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 8460b35b-1713-3865-9aee-e97404388637 | -7.2934 | -60.5713 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 01fba6c7-6a50-3e69-ad72-b1b1b93f4680 | -7.3488 | -60.5691 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d47bea33-e6d9-3dcd-8136-6422b0854208 | -7.5709 | -60.4835 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 964696a1-1f64-36ba-951f-d3aa57cecdd8 | -12.9032 | -45.8382 | 2026-09-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 6682cdfc-3bf1-3fd6-8c37-34412a1bf0f3 | -7.5895 | -60.4636 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0fbe59b0-3e35-3e2d-a9a5-5df1858cfc3a | -11.6841 | -47.5932 | 2026-09-01 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 545ee30a-0eca-36e4-9853-18e3ba1443cd | -14.478 | -52.5126 | 2026-09-01 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9d0570bd-f172-3e5a-a17e-0ccdc5c66552 | -6.9553 | -55.6151 | 2026-09-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 51d68bee-53cc-3fa0-9609-846e2c60adf1 | -6.6542 | -59.426 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e4270be3-d507-339f-93d9-0819f4980a62 | -9.4606 | -67.4531 | 2026-09-01 14:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e2e03639-b281-37f5-bc58-bde0dca4ba97 | -14.5214 | -52.2313 | 2026-09-01 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ad74dda0-79ff-3a27-9749-2347f969fd3b | -3.6216 | -60.547 | 2026-09-01 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 853added-93bb-3d7d-a106-d9c1a550a527 | -4.181 | -63.1543 | 2026-09-01 14:00:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| a20eb6c2-6e33-387e-8d39-e04240232105 | -3.9221 | -43.1291 | 2026-09-01 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 47d7fd38-6fbf-33e9-a618-7206fbbb7e8f | -6.8035 | -59.1114 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 10dfd5b8-7d04-30d5-88e9-43164e3eb818 | -6.8036 | -59.0921 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 4cd38418-f9fd-3560-bdfd-a3d3fd024141 | -14.7108 | -53.599 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 60a89f94-e5ba-34d7-9a39-5781b236feaa | -10.8627 | -45.356 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 233091ab-e6d9-3da2-aca7-d8f264f50516 | -10.0101 | -46.4386 | 2026-09-01 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |


[Clique aqui para ver as próximas entradas](README98.md)
