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
| de550c1d-cbfe-31e3-9ae4-12f4f928a619 | -3.77024 | -54.82569 | 2025-08-29 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0c5876e0-87bb-3344-8c67-a1a42b4b67d2 | -3.7422 | -48.94275 | 2025-08-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6527485d-efd5-3f19-b7a4-d378e499ae4d | -3.74507 | -49.04131 | 2025-08-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 051f2129-f196-3a7e-976d-9d0b78eb7c4f | -3.73126 | -48.9444 | 2025-08-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 13a7e057-2452-3c99-801c-f0b663e31cc0 | -5.33068 | -51.33217 | 2025-08-29 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f7e22fe-c65e-3b31-b6fd-d876a865a695 | -3.42593 | -49.04981 | 2025-08-29 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1ce0c170-6a94-38be-a77c-4006a219dc41 | -3.76119 | -54.82699 | 2025-08-29 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 81968264-337e-34d9-8a93-8ec391b4c091 | -0.75506 | -47.74447 | 2025-08-29 00:52:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 31cfdaa6-ff75-3aba-863c-b8a9c9cac67e | -3.75865 | -54.8083 | 2025-08-29 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b24bf8a0-c8ee-3ae7-9d18-b8f568d3da35 | -3.04204 | -49.42668 | 2025-08-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cf919807-a0b6-3762-b965-4bb5c5b4516f | -3.75992 | -54.81767 | 2025-08-29 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1eff32fc-bdc7-3163-88ca-35325dc1cf94 | -3.98104 | -43.25121 | 2025-08-29 00:52:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e5cad94a-95d2-3647-a054-5a56026fbe90 | -0.75784 | -47.76385 | 2025-08-29 00:52:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 19349a1f-e3dd-3fc0-94f3-9b24e1b23f06 | -3.78929 | -49.42781 | 2025-08-29 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 52ec074d-8cf3-3455-94a4-0eb325e07a80 | -3.99024 | -47.96446 | 2025-08-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 33da8ddc-876b-305f-ae9a-666f640cfc9b | -3.98372 | -47.97194 | 2025-08-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6a575649-ca86-3f33-b828-704cab5c233a | -3.98137 | -47.95535 | 2025-08-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 74f64383-4b30-3edd-9897-eaeb17a2157d | -3.98779 | -47.94802 | 2025-08-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a6830218-e6c7-329e-b0c5-36254d7b8445 | -3.76897 | -54.81635 | 2025-08-29 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a2de328d-a7ba-3a45-a42d-6bbe94db6d51 | -5.17918 | -46.08254 | 2025-08-29 00:52:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9066f993-1ac8-358a-a46b-7d9eef7f940a | -5.67646 | -52.22024 | 2025-08-29 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e1e66407-447a-36f2-885b-c88730013b6e | -5.55548 | -52.07829 | 2025-08-29 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e8b0171-6879-3c51-8106-a309c29110eb | -3.4239 | -49.03587 | 2025-08-29 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d57e9a4c-5243-3eb8-a0a7-978a23a1417c | -9.7728 | -64.2657 | 2025-08-29 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 101e91aa-d6ae-3043-9943-6a8225999a10 | -9.2178 | -60.8689 | 2025-08-29 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7049d431-ca7f-37f1-aeb3-f40e22e0d7b6 | -3.4254 | -49.0517 | 2025-08-29 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c39bebcc-37ed-3c37-844b-b345cee721ae | -10.3812 | -57.8245 | 2025-08-29 01:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 7ae6afc7-8f8c-3dc7-bcaf-e13cc8f810e0 | -13.0151 | -56.9184 | 2025-08-29 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 74c83782-bab1-3b03-b094-ddddd80cecff | -7.0381 | -44.364 | 2025-08-29 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 27ceb1f9-946e-3446-9493-b581635015aa | -9.4263 | -47.6384 | 2025-08-29 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| ddc98fd9-082e-3eb3-adaf-d404bf6b5868 | -6.5546 | -43.9221 | 2025-08-29 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 91566283-4527-35bc-9c0b-e6849ddee661 | -5.6081 | -45.0038 | 2025-08-29 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| ed1ac688-1695-3222-9a2b-7e2b39ea5cf8 | -22.6966 | -46.8382 | 2025-08-29 01:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 7a49a585-55de-3cdc-b7b7-e6870877b04b | -13.2031 | -45.2834 | 2025-08-29 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 321.0 |
| c7389a87-45a8-3ff7-8c1a-9bc436012b10 | -9.7916 | -64.2461 | 2025-08-29 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 88a14f8b-e0f6-3558-b40f-c23807783a49 | -13.1842 | -45.2633 | 2025-08-29 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 82d9d8c4-e193-3a87-ac1b-b5a195e974d9 | -17.3643 | -42.6284 | 2025-08-29 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0ac73647-dbf3-3042-83da-e38e57571032 | -3.7694 | -54.8086 | 2025-08-29 01:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f0c3db2e-800e-3f1e-ab80-137dc0db4352 | -13.2027 | -45.3066 | 2025-08-29 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| eff530c6-4ef4-30be-a100-f87cf15acc76 | -12.4345 | -63.9173 | 2025-08-29 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 163.1 |
| cd1bac5a-09c9-3358-977f-076931c08bf2 | -5.6266 | -45.0252 | 2025-08-29 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| f41a9083-8fdc-3027-8f24-e46df435c5c8 | -12.4344 | -63.9364 | 2025-08-29 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d34df59e-b95e-3166-8eec-5bfba610382a | -12.0976 | -44.717 | 2025-08-29 01:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 49770da5-25b7-3746-b667-f24464629837 | -13.558 | -46.8745 | 2025-08-29 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6f2a1ff7-2e24-3b3a-9cda-21356bf2f64b | -6.5358 | -43.9237 | 2025-08-29 01:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 44a8e44d-5fb0-3b73-b210-3261d16027f9 | -13.2036 | -45.2601 | 2025-08-29 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e1453642-8f0c-3c9a-bef4-63bd8668c2d4 | -6.7072 | -49.4774 | 2025-08-29 01:00:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e357d709-8134-369f-a145-3cd09d111f96 | -9.4618 | -60.5682 | 2025-08-29 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 1ec5cef6-be1f-3739-adc2-45a43c5b0d68 | -10.3624 | -57.8258 | 2025-08-29 01:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 56cc4657-b8dd-3233-aa32-40990493f923 | -18.1252 | -50.2586 | 2025-08-29 01:00:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 0f3f7c6d-4025-3464-8dd6-77b2c7552316 | -9.7731 | -64.228 | 2025-08-29 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e204a2db-5017-39d6-a51c-63b77d10d0bb | -9.4432 | -60.5692 | 2025-08-29 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 1e029002-b414-30eb-b3e0-e33a5565a950 | -12.9961 | -56.9201 | 2025-08-29 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| cb939478-79f2-3424-9afa-a7e0cf0885f4 | -6.7074 | -49.4561 | 2025-08-29 01:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| bf03dadb-fe11-38f1-bd83-f40327eba436 | -22.6756 | -46.8439 | 2025-08-29 01:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.5 |
| b81333c1-13f4-3c51-955d-b94d77dd622d | -9.4433 | -60.5499 | 2025-08-29 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e812f970-e9cc-3e2f-b698-b003eb096746 | -5.6268 | -45.0025 | 2025-08-29 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 338.1 |
| b5d091d3-f7a3-3c10-b7bb-2cf339b96983 | -5.627 | -44.9797 | 2025-08-29 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4105898a-118c-35de-a2b4-24d28c0d1c7f | -9.462 | -60.549 | 2025-08-29 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 43886f5c-9417-3de5-85cf-72a804966223 | -9.773 | -64.2469 | 2025-08-29 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 310.9 |
| c8dce2b2-1179-31c8-bfb5-b3a7e3557622 | -9.7915 | -64.265 | 2025-08-29 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 45426cab-26fa-3ab2-b0ed-ce8d8b8deedb | -22.6748 | -46.8681 | 2025-08-29 01:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 1d2cb946-64fb-3b4b-94b7-8c701b8505df | -7.0569 | -44.3623 | 2025-08-29 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c9cf5518-e581-3dac-85ab-a724b1c2ab18 | -12.4156 | -63.9183 | 2025-08-29 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| bd22477b-c787-366e-9a26-2f4d7b93bbc1 | -13.0342 | -56.9166 | 2025-08-29 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 456c430b-3e63-3d7c-87c7-4524a6b2c45d | -18.1457 | -50.2326 | 2025-08-29 01:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c991205c-4030-36f0-801a-6a55a2dc7d5d | -3.7693 | -54.8286 | 2025-08-29 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f57ff4bd-268f-3bb6-8f62-297a121147f7 | -17.3442 | -42.6333 | 2025-08-29 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 51535b08-b64d-3c52-ad4b-6d486fb7e60a | -8.1944 | -61.3747 | 2025-08-29 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| df9a1f0c-56e1-31da-929c-d30635325f19 | -18.1257 | -50.2363 | 2025-08-29 01:00:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 3ea163e9-e7b6-3997-ad8e-fa4a10167f02 | -18.1058 | -50.2399 | 2025-08-29 01:00:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 15a813af-698d-3441-b4fd-cdc0b81c1a2f | -13.1837 | -45.2865 | 2025-08-29 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 5b53a0ad-e090-31ed-8e82-11db458ad972 | -8.1758 | -61.3755 | 2025-08-29 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 1dabf553-f2a4-3e8e-b37b-3cf97db5b9cd | -9.2178 | -60.8689 | 2025-08-29 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 39aec382-1325-3ecb-a6a6-9a4aa122d75f | -3.7694 | -54.8086 | 2025-08-29 01:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4ac913fe-e9b9-34b6-a5bd-7b963af8dbf6 | -10.3812 | -57.8245 | 2025-08-29 01:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 0cd36557-1a72-393a-bd71-d041a68b0538 | -18.1058 | -50.2399 | 2025-08-29 01:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 61340af9-6f1f-32dc-9377-44717171666e | -13.0151 | -56.9184 | 2025-08-29 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b579a6a9-659d-3449-906c-8349ca5666bc | -9.4263 | -47.6384 | 2025-08-29 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 70a0ed2f-ad5b-33aa-b87e-54a0e90f6c61 | -17.3442 | -42.6333 | 2025-08-29 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8e8b97f1-39ad-3cae-ad89-04d4ef83e41e | -13.2036 | -45.2601 | 2025-08-29 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 15902b50-9d18-3664-9f05-e827c37c452e | -9.4618 | -60.5682 | 2025-08-29 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| c619f0b7-c0fb-32ef-af17-0f14f264c0c1 | -12.0976 | -44.717 | 2025-08-29 01:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| e608379c-3615-3c92-b0c6-5c8beccce712 | -9.7728 | -64.2657 | 2025-08-29 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 708e36e6-ad44-31a8-a06d-a4bc669bd47a | -14.2555 | -58.5084 | 2025-08-29 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c3e15933-a228-349b-8386-120e2198b810 | -5.6081 | -45.0038 | 2025-08-29 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0252c397-e5b1-3469-96dc-585112ac0f9b | -3.7693 | -54.8286 | 2025-08-29 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ace8d409-c9f1-3574-ae45-a905a5426802 | -9.4433 | -60.5499 | 2025-08-29 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 436b6f7d-1477-3084-8f1e-4fa4b7ce6361 | -18.1452 | -50.2549 | 2025-08-29 01:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 29f49ed8-b9c4-3894-a88f-732e02653013 | -5.627 | -44.9797 | 2025-08-29 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 2f6ba1ad-c1e4-33b8-ab51-4525a61e462d | -9.7731 | -64.228 | 2025-08-29 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 536be5b2-5ba8-3872-bf4e-5950f529faad | -9.462 | -60.549 | 2025-08-29 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| efbc5bb9-5000-3115-b91a-fb39686906fe | -9.7916 | -64.2461 | 2025-08-29 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 3ffe9ba1-b7ac-312a-9e07-d3e55fc6ceac | -13.1837 | -45.2865 | 2025-08-29 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 225.5 |
| e162edcc-5e97-307d-a4f3-94f625d500de | -6.7072 | -49.4774 | 2025-08-29 01:10:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| ccbc9b88-2d95-3b89-b6b0-7d6a3cef5b23 | -9.4452 | -47.6364 | 2025-08-29 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| f3b310e6-a7d0-3c3f-951b-8a07c3dd385c | -22.6756 | -46.8439 | 2025-08-29 01:10:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| b6e06147-33c7-33ea-b0d9-386d1c0044bd | -12.4344 | -63.9364 | 2025-08-29 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0bcdf9f9-f415-3b91-94b6-1c72addf64b2 | -7.0569 | -44.3623 | 2025-08-29 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 28691b41-a837-37e2-9d70-37cc87381447 | -13.2031 | -45.2834 | 2025-08-29 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 248.2 |


[Clique aqui para ver as próximas entradas](README13.md)
