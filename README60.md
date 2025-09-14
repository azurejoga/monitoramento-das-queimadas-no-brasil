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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 797a99e8-d2c7-337f-b1a5-61ea18531354 | -12.09492 | -51.38585 | 2025-09-14 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbfce5d0-2745-343a-a2e1-4f5d3c290429 | -12.24743 | -46.78761 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c0e7775-50b8-38a3-af31-1c4935238367 | -14.15382 | -46.26022 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e443dc5a-df63-3b1c-a41c-1789e94f5067 | -11.40991 | -55.35852 | 2025-09-14 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7839290-99eb-399c-ad58-51ed13e7fb36 | -12.65903 | -54.66742 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3cb8f39-0300-3bf6-83ad-39f341fee5c2 | -12.78194 | -47.9948 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bb47622-be42-3c90-833c-d03e37681370 | -10.91352 | -47.19514 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af4910b-0a65-3543-acdd-306751ff9213 | -14.19557 | -46.16119 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a928e220-5633-3b87-9038-a315bee6768c | -11.44449 | -50.76116 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a40ccad-0971-34bc-a46c-4e9174cc36a5 | -11.82076 | -50.49517 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f83f1e90-1b89-3c8d-b69b-81e89b560554 | -14.38602 | -52.92211 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01a0c37b-24e5-3fa0-a2ef-ca78c9d73e38 | -12.86275 | -52.97699 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bde5fd04-2c2c-3dd4-a999-5de30da78e07 | -11.36447 | -47.34071 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfbb0c17-bb5c-38a8-b363-d6ee21a70403 | -14.38069 | -52.9319 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de5494d4-5bf5-3e8f-a5c0-bd1dd9766720 | -11.44988 | -50.78984 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 00b06105-a11d-31a5-a5a7-58f8741ba9a8 | -11.44393 | -50.4721 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cff98ae0-4a7a-32a7-9a87-e12d61706f8f | -12.77361 | -48.01894 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bea74e5-618b-3fd2-821c-dcadfb26474f | -10.75681 | -44.77809 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec31b698-3d20-37cd-aa80-9e787c414257 | -12.67194 | -54.67758 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5864220-9af3-327a-8381-834066cecf3c | -12.77114 | -48.01221 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35b04c48-c958-3561-a339-c1bd14e28048 | -11.82319 | -50.49886 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2267d4c4-50a3-3262-bb86-a4fe418b8f0e | -11.23488 | -47.62379 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dac8e5b2-3ebd-34bb-81c3-7cee9dd73048 | -9.88809 | -58.33495 | 2025-09-14 05:08:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e4b82c-ea18-3fdb-8a8d-ff359eaced18 | -10.6662 | -48.67583 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecac9a9f-b2ef-3bf6-8c96-64a16b6595db | -12.92132 | -54.74212 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 56c34601-b6b3-3cab-bcb3-56bdba39f037 | -11.81989 | -50.48935 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca540a8a-03cd-386a-9d49-1fcc3c7481b2 | -12.70708 | -54.70741 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c99c877-0e85-3aef-a5a2-b6cb2c0a10ae | -11.4439 | -50.76536 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72310782-75f4-312a-8941-1244cdaa4c9c | -11.86449 | -50.49564 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c128b07c-131e-3545-9ead-13554624ce42 | -12.76173 | -48.00061 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 342f46ab-116d-3d41-b430-db426f14aefd | -10.76795 | -46.48258 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c4f948e-503c-3908-843b-e8e73411212f | -10.75734 | -44.77361 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1e88297-c0d9-3655-b880-f723990e4f42 | -11.28477 | -51.10225 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f42c39d6-48c5-3318-b4f6-0427c6810718 | -12.68428 | -54.66718 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fabc2029-c345-3c38-a62d-bf7ccb4e9a70 | -12.87314 | -52.95863 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c263e5f4-8b31-3466-bfeb-90c2bcc16aeb | -9.89151 | -58.33551 | 2025-09-14 05:08:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fffbc1ff-d9cf-38ff-94ac-e3941ebeabd6 | -14.61449 | -52.07307 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 586ebec3-b2e0-3e72-bb2f-254862da75d9 | -11.2497 | -44.78105 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0e71abc3-32dc-3c81-a052-f5a2ad563d9c | -12.78188 | -48.04052 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4e51e63-e4ce-3597-9412-f0e6fdcdfaea | -12.78444 | -47.99312 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a324c0f8-60b5-3e68-b4db-1bbc39df50d4 | -12.93574 | -54.74311 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57c982c8-de9c-30b8-a012-7f7c1d7851f2 | -12.68364 | -54.69574 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cbaf7599-ddfe-3337-880f-c59a72953209 | -12.9354 | -54.74424 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a72dd3dc-2669-38f3-b6ee-c808bd655622 | -9.85698 | -46.47013 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c46ea08f-2139-3355-a4bd-11d59569e898 | -12.96894 | -47.99851 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 027692cf-a2b1-3287-a62c-6a3b4b836a6a | -14.49101 | -53.89183 | 2025-09-14 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63c6a5a3-8801-3a4e-b925-1d1f72f18e0b | -12.13887 | -47.57973 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cb974ea-29f2-3c47-b748-93da2e0397f7 | -14.36891 | -52.93921 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff1c8943-fdf3-37eb-95b4-160800007645 | -8.76434 | -46.03915 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d828095-9557-3378-b346-4f57fe497d48 | -12.70356 | -54.70689 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 234f96ac-c57f-30fa-b31b-fd4ceefffded | -8.99373 | -45.77326 | 2025-09-14 05:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ad17364-7699-3244-a4c7-57f3ec6fd842 | -12.68017 | -54.67064 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e1ee1f8-6dca-36b9-be1a-07423b17f0b8 | -13.93049 | -44.85048 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| fa6f6d4e-988f-371f-b383-3dcd7fe38af2 | -13.91694 | -48.30713 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd380944-77b3-30bb-99c3-34fa50d12492 | -11.85111 | -50.49376 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| df733d8a-9f2f-3d8c-b25f-2dde994b0d08 | -12.77695 | -48.03642 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42854fd2-f249-37b9-a9d4-6bab99532c98 | -12.70004 | -54.70637 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 097677ac-54ad-340f-ab21-2222d843446b | -12.92424 | -54.74665 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da5a2bc1-42d6-34ad-9553-13dfbd7dd832 | -10.76745 | -46.4866 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 749efc4a-7751-3b9d-8395-a5e7119fd44d | -8.94824 | -46.16309 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57918549-fb8d-3c82-a1c0-ca3c6e116f15 | -11.81873 | -50.49824 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad4d7be4-65e2-30de-8e42-a46645c38800 | -12.70237 | -54.71484 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 9cc78768-b666-3917-b5c7-63b170292e5f | -12.9698 | -48.03528 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33693a80-7383-370a-b0c0-cb59261736f4 | -12.13677 | -47.59669 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71f6f635-b00d-34d1-9b6a-21836021dc53 | -14.28555 | -46.13426 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de1644be-0f8f-3a98-b25e-167320532e8f | -14.57514 | -51.40981 | 2025-09-14 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84806abc-75df-30d9-aa6f-0cedc28ad62f | -10.74973 | -44.7771 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 452d60d1-56c9-3305-8a42-bf151b1719db | -12.69122 | -54.71727 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c1d8b13c-6052-33d1-a9bb-edb8bdf7e37f | -13.91401 | -48.306 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e61bb29c-b17e-3e97-81e3-360f2f91b290 | -11.25025 | -44.76942 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 3a86edf3-d559-3a9c-a234-4b58caeb27ec | -14.27926 | -46.13697 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f792e552-365e-37e9-8d17-dfa8aa2b2da8 | -12.07882 | -47.56889 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea1e8e1-85cd-3ff8-85cd-4084947188c0 | -12.7994 | -47.14066 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ebdb26a-5b2b-3bee-8e48-25a637e92054 | -12.61421 | -57.00192 | 2025-09-14 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2146415a-0612-33ef-94b4-1b377d588a3f | -11.39683 | -50.45202 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bcf865d-b2ef-332e-bf60-407293650942 | -12.69067 | -54.69681 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1eb80dac-a6fb-31eb-8342-42c370db1b5a | -12.90898 | -54.75243 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e989bf7-89d6-37d9-99de-e9a15afc6eda | -12.97214 | -48.04197 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32e12d45-1a66-31a9-b41a-64523810ff8f | -9.85648 | -46.47396 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b127060e-d304-3992-bec1-ad4bdba34489 | -14.33703 | -46.62315 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0da9242f-da6a-3734-bcae-53e75e9358e6 | -11.28366 | -51.11018 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2264d1f5-18fa-3ec2-96ec-391df8e7a16c | -12.68126 | -54.71174 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 380a8183-7360-3711-804c-d6dfe35a9bfa | -12.93126 | -47.94978 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4df27810-d524-3605-b72c-03eba55a4784 | -12.9328 | -54.73858 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| de22dedb-bfe6-30c7-ac41-05afe90221b9 | -12.61753 | -57.00246 | 2025-09-14 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ff42b96-61d6-39de-9cb7-251022085578 | -12.78324 | -47.98401 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28bbbd76-4f3f-3c07-bc4c-82a8e678d943 | -10.96737 | -49.56504 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75b0df8b-6e8b-373f-820b-73c428366d07 | -12.91994 | -47.95301 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ae4b605-a26b-308c-b61c-f824f8645655 | -10.76375 | -44.77446 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc72c46b-0133-3239-b866-c49164366051 | -12.66782 | -54.68105 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36018b2d-3e5b-30e1-b304-23bb445e6869 | -14.63176 | -52.03877 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a86a698-ef2c-3ae7-b221-1e5e548c965a | -12.72549 | -48.02983 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57c14789-3fad-354b-9a61-49c222a91be3 | -12.04217 | -46.54033 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4007af7-4113-305b-9372-1e5baf34d931 | -14.37676 | -52.93127 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b851001-82b6-3dcf-a689-5d96e191f188 | -11.7801 | -46.62212 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fcb8cc0b-1833-3ecb-a4de-c2db8c983bda | -12.69593 | -54.70983 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9403d06e-1e24-372a-b443-6dbafa5cdea0 | -12.68191 | -54.68318 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 4059ce09-d943-3deb-bb2a-4a4363898ffb | -12.76947 | -48.00806 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8be0eb6-7ae1-3148-b43f-ca19e9dacc8c | -12.67368 | -54.69012 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5838977b-60f2-3c62-bba4-e638bf40ce7c | -12.68829 | -54.71277 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README61.md)
