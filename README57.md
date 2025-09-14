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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19841874-2f36-39c0-b9ad-4b29a7fc33a4 | -12.69414 | -54.72177 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a84a1624-a9c0-342d-a123-22646f9f4db2 | -13.01706 | -47.98516 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c80ef080-c1da-30dd-8626-397012892cee | -10.89881 | -45.56281 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dec73b8-2345-32a1-a9b8-c23a306506bc | -13.0124 | -47.9785 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b09d90a-0cdd-3c3e-bac4-c7b4617d24cf | -12.78061 | -47.9804 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8911918-e149-359d-b972-eec945fa1769 | -12.67308 | -54.69413 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84e97b98-e8e6-3f4c-b99a-f5ff0cf48a46 | -11.66398 | -46.51255 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0d5cd57-4e13-334c-a058-1db5fdff6b71 | -13.92989 | -44.85605 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b590d020-079d-3796-8778-897f1b973791 | -10.66688 | -48.67122 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b613de9-50ce-3f9a-9a2e-3a01a96a0554 | -12.67893 | -54.70322 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3c839b99-632b-3501-881d-c084fe7852c6 | -12.68131 | -54.68718 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 84a84bb2-2385-3e57-98a7-0d3d396157aa | -10.93358 | -47.35221 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| beac557c-9219-3076-be8e-d1252b70238a | -12.97629 | -48.00688 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ef30d1d-2a3d-3961-b28e-55eec27d01dd | -8.91296 | -46.16492 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cee1758-30e7-3bc1-a043-ccf753b18980 | -11.36512 | -47.33952 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f2e81b-dff4-3033-9427-7b78af0c8d72 | -12.67134 | -54.68158 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 739a6b9d-723b-3057-9544-80dda34f4af2 | -11.1336 | -45.31163 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c490e3f7-95c2-3622-a6ad-95e774e37473 | -12.78476 | -47.99058 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b917a35-5b4c-33a4-835f-09ea505141d1 | -10.90072 | -47.20789 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3037967b-50f6-3d57-afa7-239b3743fe62 | -12.8098 | -47.14999 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f294dddd-d571-3262-a38e-d9c94dedb8ba | -12.9366 | -54.73627 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c4fee94a-f418-36c5-87f4-748d73171fb2 | -12.6877 | -54.71676 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e6c971e2-e6ee-32c1-99f2-30e730821604 | -10.40716 | -48.60181 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52ad8b20-152c-3c33-8f86-9d0b520cd0c3 | -11.78469 | -46.63005 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74535e4f-c7d3-348d-ac80-1792bf57c86b | -14.20112 | -46.33385 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 101c8338-f38a-3c72-899e-a258dfe8e21b | -14.43465 | -43.21067 | 2025-09-14 05:08:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b976d7b-4c28-3f17-abad-2ef309c690f5 | -12.80261 | -47.9587 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697677ec-e3ca-35c8-8525-92fcf37d4abc | -10.91712 | -45.56556 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cdaef68a-af65-32d2-bc6d-40bc3289501c | -10.43618 | -48.61192 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11a1e036-1006-3db3-b70d-95f67c1a1490 | -14.63554 | -52.10677 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d3c6a74-0dcd-3b02-8553-54331cf6391e | -8.94256 | -46.16184 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf09afba-10b3-3693-b892-1386246e3745 | -12.68948 | -54.70482 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 73e29fea-ba30-33f7-a518-9d7befa39b37 | -8.76466 | -46.04227 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a028c83-318a-303c-b5a0-c7d4a539695b | -13.94013 | -44.82318 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 291d7d33-83c3-3974-b539-7e38f4775e71 | -11.83773 | -50.49187 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4d5f50f6-33c5-35ee-b6b2-91550440b99c | -8.76371 | -46.04382 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7407701-edbb-306d-9083-29f1e67d11ea | -11.24387 | -44.77474 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6de9faf2-149f-316c-a937-5a873058b2d1 | -14.16525 | -46.16116 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b75ba26-5518-30c0-948e-f9532878c5f5 | -12.77799 | -48.04378 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c128bd72-cbb9-37bd-ba4f-85617ab5acba | -10.32784 | -48.824 | 2025-09-14 05:08:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eef70dce-4a0b-33d7-82e4-2c2f733fbad9 | -12.77884 | -48.03711 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 438133a1-29be-39dc-a423-3c9223fca84d | -11.82823 | -50.49506 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fe49ca6b-8c5b-3c5f-8be4-1b7dc8d1c3a6 | -12.78161 | -47.99749 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 32e6a642-238b-3e66-b564-b7faea390ea5 | -7.88042 | -49.5037 | 2025-09-14 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c409a74-6c47-3ff1-9ba8-8d7ca8f66c51 | -12.69599 | -54.68534 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 7ec18968-a7f0-3371-b00a-6f9ed26480f8 | -11.86569 | -50.48675 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| a60923f5-52f3-3c18-8be3-fbff84584f2b | -11.37868 | -47.71837 | 2025-09-14 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5c9e968-1047-3281-a92e-6a3abc3b3b0b | -12.91368 | -54.74501 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc946b66-5397-3fc0-ae4a-9058bc5149eb | -12.69891 | -54.68986 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| b0e8a7ac-559a-3f3e-86cd-15bf6e57d219 | -14.62545 | -52.02182 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d53f08c-b3c5-32b9-b6c7-02607af55a5f | -11.39625 | -50.45642 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 394ff6d3-2bb2-31c7-b593-a8529f7f992f | -12.70243 | -54.69038 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| d59ee69c-9566-37d8-a65c-60a9f4506ee8 | -12.92997 | -47.96044 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccce0655-f1b9-315e-ac88-2a3fd2db0536 | -11.84101 | -50.50138 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0097858-0102-39b9-a4f8-cf37ee9037d6 | -11.24516 | -47.62899 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 910d1b68-15bb-3fc0-b2a4-5147d53d8af0 | -12.9178 | -54.74157 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebdac535-a61b-36e4-9c3f-155b9d9b4aac | -10.96849 | -49.56762 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a55db349-957b-3adb-96c8-4fd5c302b588 | -14.20069 | -46.17118 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40acee5d-521b-334e-b63b-02242541446d | -10.73808 | -46.44084 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3ea262c-5227-336c-bee1-89889a2cb4ed | -14.19966 | -46.18051 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1fa986d4-87e5-35ef-81ea-058e9654fa0c | -11.40128 | -50.45264 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bb77615-f463-32e1-bfc9-2dac47e6bea2 | -11.47669 | -50.7551 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8ecc20a0-2523-3e53-850f-300a96caec29 | -11.28421 | -51.10621 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c63fb913-02f1-3f1d-b31b-4c22e414ede2 | -12.5683 | -45.65251 | 2025-09-14 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c5c3559-8c30-3202-9d96-7d58cc3282cd | -11.3927 | -47.34202 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55bc8dfa-a444-3c1f-8ba7-1beac8884513 | -11.84219 | -50.4925 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 25523510-85fd-3b7d-b51f-35fde7bda422 | -10.76904 | -44.78471 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dd5466f-e1b1-3e58-8ea5-ba2abc0d7f8f | -11.82494 | -50.48554 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e1bdb4c-21dc-3740-a5ec-b09575b0958d | -12.97873 | -48.00749 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b8fcfb4-b2fc-3875-802e-58266ecfdf8d | -13.90619 | -48.30655 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e64cb38e-4296-3f0c-9a7a-6b4a2f529a06 | -14.61869 | -52.0409 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b41da67-3cdf-3e7c-81af-24d7fc3f2fdb | -14.31483 | -46.09476 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3a7f288-b1ca-3307-8a5b-5f7f3acd8888 | -13.96548 | -44.81456 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 64414643-3787-32e9-87db-14f703d9a75d | -11.45423 | -50.79046 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24bba2c3-ee0a-3fb4-8ae0-d4e884a91883 | -12.78012 | -48.02706 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ec9d9cb-55d7-3bd1-9fd9-74489e21c81d | -12.69718 | -54.67733 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c5d0b992-5f1e-39a5-9533-a6751f6fa883 | -8.62772 | -54.65339 | 2025-09-14 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 440c9df5-c099-3ed2-beb0-0b45aee13a8b | -10.90668 | -47.20494 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fa03e11-c4db-3149-86cf-e59168ebe3eb | -11.86895 | -50.49627 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2bf1c26b-401a-3e23-ae9e-2fc0618a8c81 | -11.3791 | -47.71504 | 2025-09-14 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aabaa799-a59d-3cd2-a742-b58689232a55 | -12.92544 | -54.73865 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 032ee0c4-0360-333c-af2f-df140ea713d7 | -12.70297 | -54.71086 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 9d3bf495-268a-3b39-9b1f-0f6b61408b49 | -12.70183 | -54.69438 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33c2209b-8865-3fb2-bb50-357f8ee2bee3 | -12.92012 | -54.75009 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 328cf619-3a49-3176-823e-a39e8c745c68 | -14.17446 | -54.0615 | 2025-09-14 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2560551-77e0-3f1d-90a5-479cbff6a527 | -12.70363 | -54.68239 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 35dd39bc-d045-3de2-bc88-dbe79ae8359a | -12.67833 | -54.70722 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c59f8fc-7d3b-3c4a-bb41-1e848bc7bce6 | -14.16463 | -46.15981 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eff506c8-435d-32a2-b5cb-20e8c7f9dcbb | -12.66841 | -54.67706 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62c3bb0c-e76c-3805-baf9-256753d099f2 | -10.97319 | -49.56825 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 169cf3ce-9f3a-356b-acb7-d984d44668dc | -14.63133 | -46.36495 | 2025-09-14 05:08:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a2843fc-a885-317a-a43d-c971af6bbebb | -12.5621 | -45.65165 | 2025-09-14 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bda5e81-3567-37ea-8e99-230f443f9f15 | -11.48105 | -50.75571 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 197622dd-6f42-3cc2-8d87-1dd3c968f0e7 | -12.78052 | -48.00658 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23487eb1-0221-336d-a42f-87124a11de51 | -13.94312 | -44.85777 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1df34d75-2b4c-3596-8dcf-8aba198d736e | -14.38217 | -52.93066 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8babfd7e-73d3-3cf4-9d14-3f0eee3c36e1 | -12.7809 | -48.0034 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6af39114-8eff-3d81-adc9-a5aa7c4cb358 | -12.94395 | -54.73617 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1a3ef7cc-6ca2-3445-b149-7e6fd52b3f12 | -13.01202 | -47.98173 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4358397-51ac-3805-8642-3f0da289e68b | -12.68185 | -54.70775 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README58.md)
