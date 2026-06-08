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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f65d22-3b05-3793-b091-18e992186dda | -10.90308 | -49.34494 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf53d918-19fb-337f-be1b-4e2b9422d0ae | -9.77972 | -47.44379 | 2026-06-08 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ef5a2aa-59dc-38b1-9d41-223b989716da | -10.85667 | -53.74023 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72dbf487-f040-332c-b1bd-6f85dae85129 | -10.11983 | -57.76448 | 2026-06-08 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 559b7f32-64a1-302c-9048-0b133128b6f5 | -10.85268 | -53.74343 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88546676-0c9f-3ed1-96a8-d171bbe34e08 | -10.12049 | -57.76055 | 2026-06-08 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4a7fb29-90f0-3107-a644-613de91c23b0 | -9.094 | -50.61037 | 2026-06-08 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06616b9b-641b-31ce-a1a5-1ba34f94484a | -10.12686 | -57.76566 | 2026-06-08 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8b7b284-8b33-3a15-9646-7868c22a161d | -10.14541 | -47.64222 | 2026-06-08 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7e69f043-e0bc-3b3b-8982-b18364719d9f | -10.77017 | -54.10012 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c25ad58-9888-3b6f-8f4e-e574d158094a | -10.57503 | -57.31985 | 2026-06-08 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 28dfe9a3-64d8-334e-9c85-3acf7971d515 | -11.08969 | -48.26722 | 2026-06-08 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cef2ad4-3b54-3788-9812-543a05c125e4 | -10.8487 | -53.74662 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ab5b484-27c9-322e-8e20-882a4bfc5ba5 | -9.78459 | -47.44445 | 2026-06-08 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30caa1fa-c45c-3e53-8913-c2da84ceb627 | -10.85325 | -53.73969 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45ceb9ef-97ee-3086-a2d6-21630bee69ae | -10.922 | -54.11256 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4ed0f26-3d0c-37f7-ab51-0927637ba1f9 | -10.47612 | -47.92859 | 2026-06-08 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 624c7893-8bbf-3fca-8e54-d7f7447b8920 | -11.02674 | -44.32088 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 405afba1-38a7-3225-9427-562309d3484f | -10.86065 | -53.73703 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 184de0c2-30d6-3197-8b2b-e8586915695d | -8.03293 | -47.76281 | 2026-06-08 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c02d813a-e9d1-3aa1-8beb-3046ac5965f5 | -10.87926 | -49.54637 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bf8dabd-e529-31f7-a9d0-7d3565243cfe | -6.98286 | -42.88285 | 2026-06-08 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| efb53c70-8d00-3bd8-b253-e6bb01ad5169 | -9.24601 | -48.23725 | 2026-06-08 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e16c6607-6468-3b66-a4d1-729c40939bb8 | -10.90192 | -49.35326 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c5bcf56-fdaf-3472-8914-aeceacf308f6 | -10.91861 | -54.11203 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c89a27-fc6d-3128-af31-da4b290ca10f | -11.03283 | -44.32165 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ce9f33c-5e06-33f0-88dd-28f931a82ee4 | -10.84814 | -53.75034 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63e66781-fbb9-3f7b-9613-86658b00c6c8 | -10.8561 | -53.74397 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11fa9eaf-b6cf-36c2-9b2d-e62a9ea9bdc7 | -10.84529 | -53.74607 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a9d7e49-38c3-397a-b4b1-c9e4a1caa8ce | -11.02731 | -44.31625 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a5b969d-cf10-3a43-bfbf-c5f6efef989b | -8.903 | -47.76891 | 2026-06-08 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f626f46d-e65f-3430-b6df-c7ea39d2a7d7 | -10.84472 | -53.7498 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac1d7b7-0620-390e-b7fb-309592a4d04d | -10.85723 | -53.73649 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9aae82d3-e42c-34ac-9440-fac951d32bae | -8.90402 | -47.77076 | 2026-06-08 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dca3fe8-2b29-389c-8271-8f71c374f648 | -10.14059 | -47.64147 | 2026-06-08 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc85e97e-28c0-315f-9a6c-da974e3e2b6f | -9.30742 | -48.97009 | 2026-06-08 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b147d870-85d9-32d3-b0aa-81d68b4573f7 | -12.07039 | -48.42522 | 2026-06-08 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f291581-f351-31e9-9800-a964da5fe571 | -9.09011 | -50.6098 | 2026-06-08 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7deb672-e6e5-37dd-ac17-a05dfa976447 | -11.79243 | -49.50814 | 2026-06-08 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27a3f7d4-7c22-3924-8745-7a9d3075546d | -11.30057 | -54.88167 | 2026-06-08 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e708b509-81b4-312c-a870-23dbd7469442 | -12.49595 | -46.26516 | 2026-06-08 05:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdbde5b0-0a5d-3584-9942-48cb341f0332 | -11.74122 | -57.82855 | 2026-06-08 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c4c0190-3e3f-3998-83fc-7cd312e0071f | -11.84246 | -52.51385 | 2026-06-08 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee07682-b63a-34dc-b295-1b71205120af | -18.90846 | -47.43447 | 2026-06-08 05:10:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7f56032-e6a7-334d-b05d-637497bae055 | -11.74057 | -57.83241 | 2026-06-08 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce1bd59a-19d1-3b81-bf4c-b00522c590d9 | -14.73492 | -52.67712 | 2026-06-08 05:10:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d7a4a85-790a-3b04-8aa5-76564ac6c5aa | -16.26724 | -60.00557 | 2026-06-08 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e9b81df-4a09-3a89-8468-7ab302f276cc | -18.90807 | -47.43818 | 2026-06-08 05:10:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9774e57-3b48-3228-b31c-da671addf60f | -18.46486 | -54.70599 | 2026-06-08 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41c098c2-1379-39cb-8576-11d26039371a | -12.49563 | -46.26774 | 2026-06-08 05:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23586976-cdba-3d42-a4a7-cb2d3602da59 | -11.89653 | -57.78315 | 2026-06-08 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3be1f463-74c4-3a57-bcbf-41cb9aef4965 | -14.29998 | -49.2415 | 2026-06-08 05:10:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2247f9eb-d677-3712-af03-c28f51455e97 | -11.55667 | -54.58217 | 2026-06-08 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc0e6d5d-1d1d-395a-adae-84185d2dc560 | -14.29936 | -49.24633 | 2026-06-08 05:10:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fbc2752-396d-3d3f-bddc-8951a638798a | -17.90278 | -51.72937 | 2026-06-08 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ab68130-0603-3aac-b327-c1864cef387a | -17.89867 | -51.72889 | 2026-06-08 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8a17bf0-d70b-3a84-aeeb-0b3e9ddc70a2 | -11.89623 | -57.7634 | 2026-06-08 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e843e0a9-50d7-3559-9a6a-4ea3a1125492 | -18.9136 | -47.43855 | 2026-06-08 05:10:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a6c1851-7d27-3e8b-a053-3c8600019e59 | -18.46435 | -54.7053 | 2026-06-08 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44942c4b-bcf3-30d4-84d8-20dc305cb53e | -12.48904 | -46.27592 | 2026-06-08 05:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30e2f835-166c-3288-b4d1-8a291d3bf0ed | -11.58484 | -58.51042 | 2026-06-08 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45a3fec3-7d51-3ee8-85ee-7fad4d13c0b7 | -14.32895 | -58.46983 | 2026-06-08 05:10:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afbf5bc1-7ac3-3804-aea3-331ae00f9112 | -14.30393 | -49.24712 | 2026-06-08 05:10:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b068f14-bb44-3ea8-89d5-e5ce59818a6f | -14.33241 | -58.47044 | 2026-06-08 05:10:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca45fd54-d344-35df-a472-d83a7e18d3cb | -18.46546 | -54.70188 | 2026-06-08 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d775b4b-f56c-3429-a5f1-6740b509bef2 | -11.54225 | -56.33515 | 2026-06-08 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff99b690-fcdb-3c69-862e-76283d24c3c1 | -14.73427 | -52.68164 | 2026-06-08 05:10:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc33c67b-20ab-3e36-92ea-9c2a7cb283e0 | -11.89969 | -57.764 | 2026-06-08 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a27db4d-2681-3fac-80ee-6be5317926ec | -12.3676 | -47.89474 | 2026-06-08 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 374e62f8-18b0-3b68-a266-192fe28208f3 | -12.22783 | -51.34415 | 2026-06-08 05:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03098288-6d73-358b-9842-63f6e564454d | -11.051 | -56.92828 | 2026-06-08 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eaa2a298-a765-32b7-b9e8-20f1f798d7b2 | -14.64299 | -58.72571 | 2026-06-08 05:10:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37d548bc-ecdd-3095-8e52-357640a303d3 | -18.46084 | -54.70473 | 2026-06-08 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbd49d71-648e-33c1-b269-3c1a0810f294 | -14.33308 | -58.46653 | 2026-06-08 05:10:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40c747d8-9798-34e2-89a9-aab7e80794ed | -12.51191 | -48.27488 | 2026-06-08 05:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11dc909c-1813-3f1d-bc84-8030811112c9 | -11.54282 | -56.33158 | 2026-06-08 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44b6ede1-e6b1-3566-864b-35200fde4e89 | -11.50843 | -56.12876 | 2026-06-08 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b40b9262-ba73-33ac-b0f6-643fc83d6e75 | -14.32961 | -58.46592 | 2026-06-08 05:10:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 574badbd-6e5f-3c38-a1e7-848713c2215c | -12.49013 | -46.26726 | 2026-06-08 05:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4e30712-7213-3d45-9805-2edc0087f3ac | -14.73363 | -52.68612 | 2026-06-08 05:10:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3cc5da2-5a71-3aa2-8c0c-8f895441a828 | -17.90175 | -51.72917 | 2026-06-08 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d733963-8c55-33e0-919b-fc41bf320511 | -11.29722 | -54.88113 | 2026-06-08 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b129e63-7e87-3daa-a12f-8683f4807bd4 | -11.55413 | -52.80754 | 2026-06-08 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a7071c9-185f-38bc-b496-03839988afbe | -11.58841 | -58.51104 | 2026-06-08 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5f87f8e-1098-3177-9223-7b22dea70a7a | -12.48944 | -46.27274 | 2026-06-08 05:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da5c7fc5-6826-32c4-8b19-c5ca63f8b2e8 | -12.51669 | -48.27555 | 2026-06-08 05:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4b70fcf-5c0a-3aae-b0f8-26595a4ba19a | -12.4898 | -46.26986 | 2026-06-08 05:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c3eee2-6784-3bb8-b320-5fa3bb028c2d | -14.30456 | -49.24218 | 2026-06-08 05:10:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4688c581-b30b-33fa-a769-7a3688c3533f | -11.5864 | -58.50985 | 2026-06-08 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a762c0b7-94d8-3bdc-9dbe-dfe374adf485 | -22.36152 | -50.64366 | 2026-06-08 05:12:00 | NPP-375D | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9524bc6-793d-35c7-badb-0ee77c7fdf91 | -20.09846 | -57.21357 | 2026-06-08 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a70869-2b3a-3e4f-9598-6942997a27ba | -21.98688 | -57.60629 | 2026-06-08 05:12:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f49e617-3f6f-319a-8149-8d0591c5c289 | -21.99023 | -57.60688 | 2026-06-08 05:12:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 378f0c73-817b-3418-b716-ded638208f24 | -21.29728 | -49.04579 | 2026-06-08 05:12:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 19e9a1a0-4420-301e-89ea-f24065b44788 | -3.49899 | -48.03492 | 2026-06-08 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca8d4bb8-c56a-31af-9438-43f79d5154bd | -9.30632 | -48.9715 | 2026-06-08 05:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee574dc3-104e-3a61-a811-044ea683306c | -9.0936 | -50.60559 | 2026-06-08 05:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3481496-289e-304a-951f-cab33370d11c | -3.5005 | -48.03702 | 2026-06-08 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f49bfeca-9a22-3c20-b859-a13a497cb5a6 | -9.30699 | -48.96627 | 2026-06-08 05:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e19fa79-e069-339d-9683-2ddf46088991 | -9.09303 | -50.60988 | 2026-06-08 05:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
