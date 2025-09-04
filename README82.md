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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e447c77d-5902-34ed-96b1-27c76ae8ceb7 | -10.46767 | -53.62473 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eca3924d-2d83-3f0f-8183-654573de40ed | -10.49392 | -46.76558 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9de42aeb-7aeb-3ccd-a569-66740741cb34 | -3.86695 | -54.60533 | 2025-09-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1b44f6e-397d-3987-81c9-99caaabdefd6 | -7.70702 | -50.31694 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcaf4271-964c-353a-942a-5de0368a8312 | -6.87096 | -58.93675 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e14d0ad-a0cd-3306-aedb-7134fbca5111 | -7.86631 | -56.99868 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d8f832a-9e7a-372c-93df-8604d25acb60 | -8.53146 | -51.31378 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5379036b-8d77-3958-baf9-c48339cc8692 | -8.3783 | -48.32955 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37a921dd-fe39-3866-841b-521895e47489 | -9.60192 | -47.05199 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 905b4081-2d27-3971-9c81-292a7f7a7db0 | -9.61081 | -47.03518 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d2a5f89-4920-36fe-bb87-dcf2720d93b0 | -4.99908 | -56.25721 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 36050ec4-60b6-3683-84a3-8016f761f7d5 | -7.70661 | -50.32 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16b9d64c-9fef-3aaf-ab7e-8dc71cbcf8d3 | -9.32953 | -55.21968 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d117232c-7295-362b-829b-07a4c2884aa9 | -5.3034 | -55.97604 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa3224d9-0051-3828-a8c5-33536d01d3c3 | -6.83632 | -46.39505 | 2025-09-04 05:16:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 468cf307-da82-322a-83d5-4e3c4abbc588 | -10.48633 | -46.77082 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63745dac-805e-3a19-a4b1-f12532111679 | -8.06249 | -52.37158 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41c012e7-1c8c-371b-817d-e3ebeb1af0ab | -6.03013 | -46.67873 | 2025-09-04 05:16:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06b92c9b-0c6a-3538-b582-ed7f7c368a5c | -6.66725 | -60.0311 | 2025-09-04 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0ad19d1-e13e-369b-be99-a139acc201e5 | -6.47046 | -53.40296 | 2025-09-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b28a845d-ebe9-34c3-bbcf-c7aae4eee068 | -3.64199 | -59.12102 | 2025-09-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7708defa-cd53-366b-8e1a-e37ec085df7b | -6.79383 | -58.99547 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e94df80-2f2b-3428-b0fa-3c2c6a063155 | -5.02239 | -56.11303 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 276da4a4-f4b7-30f4-98ff-c58c684ed1ca | -6.8336 | -59.36707 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 314d53b5-3866-3f3b-a923-c2049349e940 | -6.75287 | -58.73679 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7da59d38-1256-3f5b-a766-11f411d20ba2 | -10.75401 | -48.27031 | 2025-09-04 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a35839f-4e2e-3fd7-abea-76519e6326fa | -3.4346 | -59.57093 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13c01ad6-09ac-3cfd-8559-4ee7a5844ee6 | -6.46903 | -55.88554 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fff7174-f268-3efa-9d6a-312513b3fcbb | -8.53491 | -51.32541 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0d54b9f-381b-3084-b962-eacaeb8bd745 | -7.26577 | -57.56018 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8c91f48-73b6-3708-8184-aa8f4bf9f46c | -7.30747 | -57.15336 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39cac7f1-a0d8-30b7-9694-f2562368931a | -6.74624 | -58.73576 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 613ea06e-0090-3516-8e9d-8c158ab0cbfa | -8.37771 | -48.33399 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acb32c6f-aa33-3f31-b88f-9c702e9ed104 | -6.68894 | -48.41301 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f08f22-163b-3c94-82f6-179e6ddb5574 | -8.058 | -52.37428 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95ff9b12-5779-3eae-b6f6-55ecd88f0af2 | -10.06391 | -54.79141 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 359389bf-c6f9-3b9c-8f93-563a9c73e57f | -7.69135 | -48.73568 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0961d9-5678-3b85-8eaa-ce8fc58cef30 | -7.01824 | -59.65947 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc07e139-4e5b-3d10-a5e0-6348b9b3c62b | -10.09698 | -54.76707 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68774516-9be2-34c6-8472-991668695cfe | -5.28455 | -55.9569 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0362a2d6-d430-356f-922e-70ad44f4ff9b | -9.97927 | -51.62896 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2933ae9-2bb5-3fa5-9c55-7ee43ed82bd7 | -6.67871 | -48.40023 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 04e27ad8-2d6d-3bf3-9984-1d8b81fd603b | -6.74679 | -58.73229 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b37fe74-f675-3de0-939e-dcfeab1757e9 | -10.50379 | -50.44822 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0de5592f-0b5a-3b43-9200-ed0c5f5779c6 | -3.42789 | -59.56988 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49c6bf22-6756-351e-ad03-51c724a69389 | -6.67765 | -48.4078 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5403e81a-ce29-3ef7-833f-7c612a570bb5 | -6.68087 | -48.41421 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cba8e543-7258-3d03-8dc3-f445ee7cf735 | -9.1165 | -61.48786 | 2025-09-04 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba859d75-0e80-368c-8407-62aabb6940f6 | -9.96815 | -51.63129 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acbbef6-452a-324d-ab7e-23952b0e5953 | -5.27747 | -55.95578 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 08e8e965-4a3f-3b34-9a6d-35bfd2d2686a | -6.78379 | -63.13588 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0f099ce-df96-3ef7-88b6-cf81496e1993 | -9.33801 | -55.21584 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72f2bb11-8284-36b3-acd1-07d3428cb238 | -10.15315 | -46.26739 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 367ccf7b-8932-397a-a6c7-9f741661ce4f | -8.38019 | -48.3227 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f75b786-c4be-3834-984f-b4664568c454 | -8.54041 | -51.3273 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cb871cf-586b-3585-a412-9a383d68e570 | -6.4612 | -55.88859 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1afec928-b2a5-34c5-bdbe-ff804535614b | -10.95118 | -50.99851 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0889b55f-17bd-3410-9b40-0c75d9ec23ec | -9.0618 | -46.98931 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b810c21-2543-3138-a523-b156521792e4 | -7.68999 | -48.73777 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a7a2487-2242-3330-8918-cbfe83637c3d | -9.33483 | -55.21042 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2f7c000-aea9-3638-aaea-a1b617aa1396 | -6.76486 | -63.13266 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 58b0043b-a44f-3276-a26a-4ef466aac1ba | -10.09256 | -54.79897 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 156e88b1-60b2-3840-881e-a5fe647dcc83 | -9.06844 | -46.99022 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 804eeb09-7d32-3251-a232-b1766ed95dc8 | -5.26715 | -50.76406 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5c42f44-5408-38ab-b290-ade3d4edcc25 | -8.08035 | -47.59222 | 2025-09-04 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 336f37fe-8c59-3f76-9f6c-eba0ebc833e6 | -6.22502 | -55.93316 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a84075-61bc-34a1-8bc1-647b075f4f1c | -5.69364 | -45.17731 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21d1cefc-0240-395b-b245-7577585d6b89 | -6.84049 | -59.15178 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f0c238a-7e6b-3028-b256-149c66d81c60 | -10.15071 | -55.15961 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c434cfd3-d788-387b-814d-3cd5c56bc222 | -7.68024 | -48.72969 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e17771bf-ec90-370e-8fee-f2705d8b9bed | -4.83295 | -55.79092 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e0d4cc7-ecca-323e-87cf-df12e029d9c3 | -5.94033 | -55.71621 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f5b116a-c4d7-3170-a018-e6aaf4bbe916 | -10.09196 | -54.7736 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b40ae9e3-53a3-35dd-b1de-6531d1bdf2de | -10.51104 | -50.43476 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89defe30-21c6-3846-acd2-cfd6d386f619 | -5.28101 | -55.95633 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 281a2334-bb10-30a1-9632-770bcb224cfe | -6.75806 | -63.12673 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1addefc0-926e-368b-ae37-5ae923450246 | -6.67714 | -48.41142 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5d546152-df8f-378d-85c6-fd84a3ba6d70 | -4.99848 | -56.26105 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a97edddf-b108-33a0-8dcc-36d165d7350b | -6.46841 | -55.88966 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35fd76b9-6350-3ae9-972d-2a015da19ea1 | -6.87768 | -59.98898 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fde78a96-d6a4-3ea4-8331-6e6b104a675c | -5.6946 | -45.17025 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0f6a278-fc1f-30b4-b297-e034c41b6454 | -10.09167 | -54.77017 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0140f234-ea26-3c00-9edd-125e9bd133ad | -9.49189 | -57.81488 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41864574-754d-3353-86b1-fc5401161b99 | -6.02588 | -46.66133 | 2025-09-04 05:16:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3393b5d9-7b12-3484-8e51-9b2646a76387 | -6.88448 | -59.08782 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bdb5328-452b-32b8-883a-4022c4d9c250 | -5.61529 | -57.36444 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bc1f2d3-dcf9-3360-b405-4a4fd9ea4f83 | -10.45526 | -54.78537 | 2025-09-04 05:16:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cdaf936-64ec-388b-8591-e3512b64a8d1 | -7.69245 | -48.72762 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65cce772-fa35-3873-85b3-c8054ee5aecc | -8.37905 | -48.33176 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b3656b4-77ca-324b-9e2f-363e3095c700 | -5.65139 | -51.27105 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7288947-d873-3815-9a5d-2321672f4e75 | -7.27312 | -57.55754 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18ef12fc-483b-3ec8-b692-23b1b394ffa5 | -6.46481 | -55.88913 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6483e5b9-3122-3f03-9003-716cac8d7000 | -8.35837 | -48.34022 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84b7a869-e051-325e-aaee-7df701168569 | -5.02215 | -56.10951 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17d87be7-6577-3825-aaa2-f01ceb2b7178 | -8.37243 | -48.33539 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0945b0ba-efe0-3fb8-b5b6-e00fb657de6f | -10.46185 | -50.385 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f394b8a4-11d9-3c7d-b218-aa1d5822106d | -8.52569 | -51.31868 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4078839-b3d5-3981-a809-f44e6a7ffa79 | -6.9471 | -62.99123 | 2025-09-04 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f91e0f3-87ed-3696-9656-407145572a89 | -6.93874 | -59.64742 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f4cbc76-f1c5-3672-b873-ea4845ca675f | -5.00119 | -56.25313 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |


[Clique aqui para ver as próximas entradas](README83.md)
