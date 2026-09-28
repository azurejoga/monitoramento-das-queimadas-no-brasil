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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c8facc4-74e0-3d52-bbf4-3d74d0c863f9 | -10.22121 | -50.01318 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e87317ed-1cac-3485-a53b-8348ad1fd3d0 | -7.68708 | -44.87249 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 98dd6141-4d13-3b18-b1c4-6740b629605c | -7.1542 | -39.31995 | 2026-09-28 16:26:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 868ad30e-36a8-3ae0-9695-bdb487ff4d9b | -10.20558 | -49.98186 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f261d682-45fd-3b04-bec2-f77fb8c44855 | -9.51283 | -46.37175 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b2596ea-8cbf-39c9-a33d-763da14fe9d0 | -10.70309 | -44.4343 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 63296f6e-69ad-3951-9ab1-a4026050add1 | -10.79466 | -48.74522 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b534a813-b434-35be-a045-c80ca2221dba | -9.33605 | -46.54035 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 429ef9f0-9c09-3234-afe2-45b02ee8ada5 | -4.87347 | -45.47014 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d20afdfb-953a-3c2e-8088-f7a241c4e35e | -11.36895 | -47.44058 | 2026-09-28 16:26:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b130e13-edc2-3653-a5f6-c6d4d9129767 | -10.8938 | -50.69228 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2e55de2d-59a4-3aa5-b36e-01563c2b632d | -9.38945 | -46.38996 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 833e9421-669a-37d5-9e6f-167d2807be3f | -7.38968 | -42.12112 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3895f59d-6690-31d1-acd3-dd0d2b40e404 | -8.27366 | -54.70758 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 66af5fab-98fa-37f9-998e-7e3a8184be7b | -5.55495 | -48.45601 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5aaa80fa-45e8-3163-b9bb-61f1cd7cc905 | -6.19889 | -52.90989 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9e26abb-346f-39f9-864e-3908274a91e5 | -9.98003 | -45.34463 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d0289490-dfea-3495-93e5-1f25c6cdd2d1 | -9.07263 | -47.18218 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 688a6a8e-46b1-35ba-a174-2e343db00929 | -11.4718 | -49.74894 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c1fb138c-11d9-3cc9-9148-38a6e04463d5 | -11.07082 | -48.89459 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cf89883c-1756-310e-ba73-549745ebd6e8 | -7.69301 | -54.76275 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 5a0de46e-e50f-3d6a-9daa-e07b67cf3815 | -11.17917 | -50.62482 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 725df73b-ca1c-348b-aa94-c803f5c3219a | -7.38153 | -44.76447 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 82576b24-c101-3e65-b958-c395dc59fd03 | -7.84643 | -46.93373 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| de091a08-833b-3f1f-a7d7-9403261325e9 | -10.84471 | -50.59757 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ea5359e5-e179-3e4f-80c6-108db00b3e8d | -9.77337 | -44.84263 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb1adc65-f786-341d-98f9-3f8d6e60dbfc | -10.95434 | -43.88067 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b1458741-2b48-3f46-a2b2-92c8a8118aa7 | -5.73707 | -45.02374 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0f63fffb-72a9-385d-8bc8-04adf4640b8f | -9.44306 | -41.81222 | 2026-09-28 16:26:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 229352dd-a978-3610-a1fe-51e2790a2d36 | -8.52668 | -45.84879 | 2026-09-28 16:26:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 53947e96-94ae-350c-8530-f0ef99dd472b | -7.53799 | -50.93005 | 2026-09-28 16:26:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4462b6a-4885-39bb-b5db-0f4ca0f23c3e | -10.95506 | -50.66782 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f05ee82b-f0ae-30d8-b902-2f590f51b57c | -9.51533 | -46.36153 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b7a1c43d-fac1-346c-848a-6fb9805c2129 | -3.88293 | -40.83623 | 2026-09-28 16:26:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e8cfc7e6-b885-3782-98ee-58429f2ac29a | -6.69416 | -45.64146 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4eab5e52-ea48-3a88-8f51-731b1b35bdb7 | -7.45472 | -44.59883 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e07c51dc-46f2-3e6d-af66-55040fe0a72b | -7.58085 | -44.78975 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f04ac2b7-38a8-3486-8ec0-00d775743ce8 | -9.08409 | -46.54939 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f164a93-2976-3abd-9861-75d5ae8d5657 | -9.83012 | -45.26086 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c647dee-5fc3-3f01-9ed0-5bf5b610696f | -8.58327 | -44.85353 | 2026-09-28 16:26:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1a915231-efc8-3354-88ff-7e0f2bed3e96 | -6.46331 | -45.90867 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 195b93d3-b6c3-34ce-9699-627e7eb79d2b | -10.51612 | -45.36117 | 2026-09-28 16:26:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2680cf36-5c83-3878-b294-359e62f03e48 | -9.52573 | -46.37989 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0b116765-05c1-3138-93a6-7bd2a85fa841 | -6.69173 | -45.67504 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e9c901be-e70e-3727-946f-6defe2c59eb4 | -7.6352 | -44.61477 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2d60c7c-bdd2-33ba-80d7-c26b28e647ca | -8.58278 | -45.0977 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5921a15b-5561-368f-af34-b281ac266352 | -11.45499 | -49.74633 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6b60587a-9921-3679-90d2-9fedc223f7b9 | -7.47311 | -44.58078 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9abbde06-5611-3b65-9cc0-3172424b24af | -7.62436 | -45.52748 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 668cc266-4d6c-37d0-b84e-9e84825fd627 | -9.50249 | -46.35365 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e56cbf79-7f31-3198-8ad5-afa785ba5b7a | -6.35482 | -45.78455 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 19ca6a46-4017-3ce5-b4ec-3e482695b8b4 | -9.32006 | -46.56757 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d32d34cc-c74a-30f3-b3b3-16789da76750 | -7.52359 | -44.89623 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e0f4b707-8abd-30bf-82e4-86175f7af63c | -7.25337 | -43.36635 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 772e0da7-89cc-3f64-a30d-d6b648db6f6f | -8.6443 | -45.758 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 487039f5-a680-3f19-9e6e-f45de7c46805 | -7.23351 | -44.85625 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2fd666aa-6f72-3260-90b3-a74096e06561 | -7.3264 | -55.00332 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d2f2e38-8071-3119-a3b1-cceb183ec952 | -9.51667 | -46.37122 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1c7eaf49-6a19-3f9d-8651-99920d747889 | -10.99623 | -50.69875 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 930a4f33-57e8-3caf-946d-46dbe9a71c4d | -11.76178 | -50.76146 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e74ae65e-5ce2-34d1-a71c-ecda7c7b252c | -6.1919 | -41.65991 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d6689b82-515e-34c8-9cd8-2f160956fbf8 | -7.82566 | -55.13205 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e1bcb16b-9343-356e-8906-9aff9d62a72a | -11.71753 | -50.66517 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72a2f6d5-f302-3372-b07e-11d7a3be1a7c | -7.29272 | -44.3079 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f081b87d-3cea-35f8-8a2b-c3d4100bd68f | -6.36497 | -45.80361 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| c48d1b7d-4ffc-3ef3-98a4-f3d9f4faa849 | -8.57336 | -45.7596 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 538850ad-a18f-3547-ade3-2fd7dbc8ba74 | -7.34188 | -42.07606 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| bd9d7bf5-c56d-31b2-ad23-e95928e07ee8 | -10.65173 | -50.7195 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 508fcfde-f9bd-3762-83c6-f4c51dd3d62e | -10.20921 | -50.03795 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6a9ad45-a08f-3c55-a4c7-e7d0bd0045f1 | -7.68577 | -54.75809 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f2e61e6-e9a6-3968-8167-2ad2f062b336 | -11.83268 | -50.64571 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 54bee633-1e5e-36c6-b0b5-48109ba8dec7 | -7.37857 | -42.13705 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d7855e60-bf69-3cbc-912e-c7900c4bb4f2 | -6.94782 | -41.61457 | 2026-09-28 16:26:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 5d75a092-4ced-3d2b-8354-104d410ddafa | -3.88233 | -40.8323 | 2026-09-28 16:26:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3567ad94-7b3c-39d9-a64f-125ce59d5a15 | -6.69946 | -45.67804 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 37e60e25-5e0a-3dd0-892f-a4b18f1ba266 | -3.67671 | -38.95757 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 01c3b641-e053-311d-9709-dbaae5114055 | -10.20347 | -49.9925 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ac0f281f-9258-3edb-8da4-9205e627b059 | -5.80399 | -43.62978 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7fbbe9cb-594c-3e68-9bd2-1286f223e3c8 | -10.95746 | -50.68724 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8bcef333-a936-3626-a700-e8a132d3589c | -11.16006 | -48.31829 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b4d78d9d-7b58-3d4d-843b-27cf185fed2b | -7.25564 | -43.35885 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 900d46e0-0b32-36f1-ac64-d1a086522e75 | -6.70303 | -45.67753 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a0c7daa3-6c3a-3486-a115-f67964807b19 | -4.28857 | -38.41571 | 2026-09-28 16:26:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 480fe5f5-8480-372a-bf0f-aef71d3fa519 | -5.60942 | -42.93053 | 2026-09-28 16:26:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8da3e386-5c0f-3d09-8fd2-da49b235fd8c | -9.76983 | -44.84317 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 4d7e7e07-96ce-35f3-9269-819af88cdbda | -7.26313 | -43.31831 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 978e92a4-f5a2-36d6-9497-4a8bc3a5d53c | -9.51033 | -46.38203 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3bf23002-a1e6-3486-b749-5ba8854f39c2 | -10.10437 | -43.94963 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0f0a8303-e22b-3e5b-b74d-e76995c955e1 | -11.12901 | -51.17232 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9a8da713-8c5c-3b15-aea2-e12c5df585ea | -7.33857 | -42.07658 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 76604ae2-062b-349f-a4da-da353291e3a4 | -7.25512 | -43.35535 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37c95f94-9b2a-36a4-8eb4-69ccc5696209 | -7.6339 | -45.5177 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0aa6a6d5-17c6-3456-92d3-728e51540e2c | -3.22062 | -42.80269 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 87890d09-5e19-39ae-acd8-c11c7ae6c976 | -7.39814 | -42.62103 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 9b1aa2d2-9a1f-397e-ab5a-3ff6e0d93cac | -9.31028 | -46.44032 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7e5e1c45-570a-3f70-8cb8-56001b0cfd87 | -9.77752 | -44.82129 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| ab944365-49bd-3f86-8766-17a03769f927 | -6.16942 | -52.82291 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0debaa1d-747e-3197-9368-d943a9b74dd3 | -9.3352 | -46.42209 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b132a60c-1e56-3055-81ee-8b7801fd6d76 | -3.42082 | -42.6037 | 2026-09-28 16:26:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0aca904c-ed52-3650-92f8-e2ba24ffc1fc | -11.14442 | -50.06149 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |


[Clique aqui para ver as próximas entradas](README122.md)
